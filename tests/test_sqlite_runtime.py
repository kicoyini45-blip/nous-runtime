from __future__ import annotations

import sqlite3
import threading
import time

import pytest

from nous_runtime.sqlite_runtime import SQLiteRuntime


def test_sqlite_runtime_wal_foreign_keys_batch_plan_and_metrics(tmp_path):
    runtime = SQLiteRuntime(tmp_path / "runtime.db")
    with runtime.connect() as connection:
        assert connection.execute("PRAGMA journal_mode").fetchone()[0] == "wal"
        assert connection.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        connection.execute(
            "CREATE TABLE items (id INTEGER PRIMARY KEY, value TEXT NOT NULL)"
        )

    assert runtime.batch(
        "INSERT INTO items(id, value) VALUES (?, ?)",
        [(1, "one"), (2, "two")],
    ) == 2
    plan = runtime.explain_query_plan(
        "SELECT value FROM items WHERE id = ?", (1,)
    )
    checkpoint = runtime.checkpoint()
    runtime.record_backup()
    metrics = runtime.metrics()

    assert plan
    assert checkpoint["duration_ms"] >= 0
    assert metrics["database_size"] > 0
    assert metrics["integrity_status"] == "ok"
    assert metrics["transaction_p95_ms"] >= 0
    assert metrics["last_backup_age_seconds"] is not None
    with pytest.raises(ValueError, match="read queries"):
        runtime.explain_query_plan("DELETE FROM items")


def test_sqlite_runtime_recovers_from_temporary_lock_with_bounded_retry(tmp_path):
    runtime = SQLiteRuntime(tmp_path / "runtime.db", busy_timeout_ms=10)
    runtime.execute("CREATE TABLE items (id INTEGER PRIMARY KEY)")
    blocker = sqlite3.connect(runtime.path, check_same_thread=False)
    blocker.execute("BEGIN EXCLUSIVE")

    def release_lock():
        time.sleep(0.08)
        blocker.rollback()
        blocker.close()

    thread = threading.Thread(target=release_lock)
    thread.start()
    try:
        runtime.execute(
            "INSERT INTO items(id) VALUES (?)",
            (1,),
            retries=10,
        )
    finally:
        thread.join(timeout=1)

    with runtime.connect(readonly=True) as connection:
        assert connection.execute("SELECT COUNT(*) FROM items").fetchone()[0] == 1
    assert runtime.metrics()["busy_retries"] >= 1
