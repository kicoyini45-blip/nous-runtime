# -*- coding: utf-8 -*-
"""Nous Runtime CLI -`nous` command."""

from __future__ import annotations

import json
import sys
import os

try:
    import typer
except ImportError:
    print("Error: typer is required. Install with: pip install typer")
    sys.exit(1)

from nous_runtime.cli.decision import register_decision_commands
from nous_runtime.cli.policy import register_policy_commands
from nous_runtime.cli.profiles import model_app, profile_app, provider_app as profile_provider_app
from nous_runtime.agent.cli import agent_app
from nous_runtime.version import __version__ as _V

app = typer.Typer(
    name="nous",
    help=f"Nous Runtime v{_V} - long-lived intelligent runtime",
    invoke_without_command=True,
)


@app.callback(invoke_without_command=True)
def _shell_callback(
    ctx: typer.Context,
    json_output: bool = typer.Option(False, "--json", help="Emit JSON Lines"),
    quiet: bool = typer.Option(False, "--quiet", help="Suppress terminal chrome"),
    session_id: str = typer.Option("", "--session", help="Reconnect to a session"),
    no_color: bool = typer.Option(False, "--no-color", help="Disable color output"),
    show_version: bool = typer.Option(
        False,
        "--version",
        is_eager=True,
        help="Show version and exit",
    ),
):
    """Enter the persistent terminal interface when no subcommand is given."""
    if show_version:
        typer.echo(f"Nous Runtime v{_V}")
        raise typer.Exit()
    if ctx.invoked_subcommand is not None:
        return

    if no_color:
        os.environ["NO_COLOR"] = "1"
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")

    interactive = bool(sys.stdin.isatty())
    if interactive and not json_output and not quiet:
        try:
            from nous_runtime.project.workspace import find_workspace, init_workspace

            workspace = find_workspace()
            if workspace is None:
                typer.echo("No Nous workspace found.")
                typer.echo("Create .nous for this project? [Y/n] ", nl=False)
                try:
                    answer = input().strip().lower()
                except (EOFError, KeyboardInterrupt):
                    answer = "n"
                if answer in ("", "y", "yes"):
                    workspace = init_workspace()
                    typer.echo(f"  Workspace created: {workspace}")
                else:
                    typer.echo("  Continuing without a project workspace.")
        except Exception:
            pass

    from nous_runtime.cli.shell_v2 import run

    run(
        json_output=json_output,
        quiet=quiet,
        session_id=session_id,
        interactive=interactive,
    )

# Subcommand groups

pack_app = typer.Typer(help="Manage packs")
app.add_typer(pack_app, name="pack")

provider_app = profile_provider_app
app.add_typer(provider_app, name="provider")

app.add_typer(model_app, name="model")
app.add_typer(profile_app, name="profile")

capability_app = typer.Typer(help="Manage capabilities")
app.add_typer(capability_app, name="capability")

project_app = typer.Typer(help="Project workspace commands")
app.add_typer(project_app, name="project")

memory_app = typer.Typer(help="Inspect project memory")
app.add_typer(memory_app, name="memory")

retrieval_app = typer.Typer(help="Manage retrieval indexes")
app.add_typer(retrieval_app, name="retrieval")

retrieval_index_app = typer.Typer(help="Manage retrieval index generations")
retrieval_app.add_typer(retrieval_index_app, name="index")

decision_app = typer.Typer(help="Inspect runtime decisions")
app.add_typer(decision_app, name="decision")

policy_app = typer.Typer(help="Manage runtime policies")
app.add_typer(policy_app, name="policy")

app.add_typer(agent_app, name="agent")

inspect_app = typer.Typer(help="Inspect runtime snapshots", invoke_without_command=True)
app.add_typer(inspect_app, name="inspect")

inspect_memory_app = typer.Typer(help="Inspect memory snapshots", invoke_without_command=True)
inspect_app.add_typer(inspect_memory_app, name="memory")

inspect_retrieval_app = typer.Typer(help="Inspect retrieval snapshots", invoke_without_command=True)
inspect_app.add_typer(inspect_retrieval_app, name="retrieval")

register_decision_commands(decision_app, inspect_app)
register_policy_commands(policy_app)

# Context Runtime commands (Phase 3)
try:
    from nous_runtime.context.cli import register_context_commands
    register_context_commands(app, inspect_app)
except Exception:
    pass  # Context commands unavailable, core CLI still works

# Evaluation Runtime commands (Phase 4)
try:
    from nous_runtime.evaluation.cli import register_evaluation_commands
    register_evaluation_commands(app, inspect_app)
except Exception:
    pass  # Evaluation commands unavailable, core CLI still works

# Experience Runtime commands (Phase 5)
try:
    from nous_runtime.experience.cli import register_experience_commands
    register_experience_commands(app, inspect_app)
except Exception:
    pass  # Experience commands unavailable, core CLI still works

# Agent Network commands (Phase 6)
try:
    from nous_runtime.network.cli import register_network_commands
    register_network_commands(app, inspect_app)
except Exception:
    pass  # Network commands unavailable, core CLI still works

# Phase 8 Runtime Closure commands
try:
    from nous_runtime.interaction.cli import register_interaction_commands
    from nous_runtime.model.cli import register_model_runtime_commands
    from nous_runtime.runtime.cli import register_runtime_commands
    from nous_runtime.workspace.cli import register_workspace_commands

    register_interaction_commands(app, inspect_app)
    register_workspace_commands(app, inspect_app)
    register_runtime_commands(app, inspect_app)
    register_model_runtime_commands(app, inspect_app)
except Exception:
    pass  # Phase 8 commands unavailable, core CLI still works

# Release-candidate capability commands are isolated so optional adapters do not
# prevent the core CLI from starting.
for _module_name, _register_name in (
    ("nous_runtime.connectors.cli", "register_connector_commands"),
    ("nous_runtime.plugins.cli", "register_plugin_commands"),
    ("nous_runtime.knowledge.cli", "register_library_commands"),
    ("nous_runtime.workflow.cli", "register_workflow_commands"),
):
    try:
        _module = __import__(_module_name, fromlist=[_register_name])
        getattr(_module, _register_name)(app)
    except ImportError:
        pass

debug_app = typer.Typer(help="Debug and diagnostic commands")
app.add_typer(debug_app, name="debug")

# Developer tools -wrapped in try/except so dev failures don't break core CLI
try:
    from nous_runtime.cli.dev_commands import dev_app
    app.add_typer(dev_app, name="dev")
except Exception:
    pass  # `nous dev` commands unavailable, core CLI still works


# Top-level commands

@app.command()
def init(
    path: str = typer.Option(".", help="Project directory to initialize"),
    wizard: bool = typer.Option(True, help="Run interactive setup wizard"),
):
    """Initialize a new Nous Runtime workspace with interactive setup."""
    if wizard:
        from nous_runtime.cli.wizard import run_wizard
        run_wizard()
        return

    workspace = os.path.abspath(os.path.join(path, "nous_workspace"))
    os.makedirs(workspace, exist_ok=True)
    os.makedirs(os.path.join(workspace, "packs"), exist_ok=True)
    os.makedirs(os.path.join(workspace, "data"), exist_ok=True)

    # Initialize the database so all required tables exist before any
    # pack operations. This can run inside or outside a workspace.
    try:
        from nous_runtime.services.database import run_migrations
        n = run_migrations()
        if n > 0:
            typer.echo(f"  Database initialized ({n} migrations applied)")
        else:
            typer.echo("  Database is up to date")
    except Exception as e:
        typer.echo(f"  Warning: database init skipped ({e})")

    typer.echo(f"Nous Runtime v{_V} - initialized at {workspace}")


@app.command()
def demo():
    """Run the first-experience demo: Goal -> Plan -> Execute."""
    from nous_runtime.cli.stream import TraceDisplay, Spinner
    import time

    typer.echo()
    typer.echo("Nous Runtime - Demo (built-in)")
    typer.echo("-" * 32)
    typer.echo()

    trace = TraceDisplay()

    trace.add("Goal: Demonstrate Runtime pipeline", "running")
    time.sleep(0.3)
    trace.update(trace.steps[-1], "done", "User intent -> structured goal")
    typer.echo(trace.render())
    typer.echo()

    spinner = Spinner("Planning...")
    spinner.start()
    time.sleep(0.5)
    trace.add("Plan: Resolve capability graph", "running")
    time.sleep(0.3)
    trace.update(trace.steps[-1], "done", "model.reason -> built-in demo provider")
    spinner.stop("done")
    typer.echo(trace.render())
    typer.echo()

    spinner = Spinner("Executing...")
    spinner.start()
    trace.add("Execute: model.reason via built-in demo", "running")
    time.sleep(0.4)
    trace.update(trace.steps[-1], "done", "Demo pipeline complete")
    spinner.stop("done")
    typer.echo(trace.render())
    typer.echo()

    trace.add("Audit: Record experience", "running")
    time.sleep(0.2)
    trace.update(trace.steps[-1], "done", "Stored for provider optimization")
    typer.echo(trace.render())
    typer.echo()

    typer.echo("Demo complete! (using built-in demo provider)")
    typer.echo()
    typer.echo("No external API key required for the demo.")
    typer.echo("Configure a real provider: nous provider setup")


@app.command()
def version():
    """Show Nous Runtime version."""
    from nous_runtime import __version__
    typer.echo(f"Nous Runtime v{__version__}")



@app.command("status")
def status_cmd():
    """Show Runtime status."""
    from nous_runtime.kernel.runtime import Runtime
    from nous_runtime.services.packs import count_packs

    status = Runtime().status()
    typer.echo(f"Nous Runtime v{status.version}")
    typer.echo(f"  Running:      {status.running}")
    typer.echo(f"  Providers:    {status.providers}")
    typer.echo(f"  Capabilities: {status.capabilities}")
    typer.echo(f"  Packs:        {count_packs()}")
    typer.echo(f"  Devices:      {status.devices}")
    typer.echo(f"  Events:       {status.events_total}")
    typer.echo(f"  Jobs pending: {status.jobs_pending}")


@app.command("doctor")
def doctor_cmd():
    """Run environment diagnostics."""
    from nous_runtime.cli.doctor import format_report, run_diagnostics

    typer.echo(format_report(run_diagnostics()))


@app.command("trace")
def trace_cmd(
    limit: int = typer.Option(20, "--limit", help="Maximum traces to show"),
):
    """Show recent reasoning traces."""
    from nous_runtime.services.traces import get_recent_traces

    traces = get_recent_traces(limit=limit)
    if not traces:
        typer.echo("No traces.")
        return
    for item in traces:
        trace_id = item.get("trace_id") or item.get("id") or "?"
        outcome = item.get("outcome") or item.get("status") or "unknown"
        goal = item.get("goal") or item.get("summary") or ""
        typer.echo(f"{trace_id} [{outcome}] {goal}")


@app.command("chat")
def chat_cmd():
    """Open the interactive Nous Runtime shell."""
    from nous_runtime.cli.shell_v2 import run

    run()

@pack_app.command("list")
def pack_list_cmd():
    """List installed packs."""
    from nous_runtime.services.packs import list_packs

    packs = list_packs()
    if not packs:
        typer.echo("No packs installed.")
        return
    for pack in packs:
        typer.echo(f"{pack.get('name', '?')} {pack.get('version', '')}")


@pack_app.command("install")
def pack_install_cmd(
    path: str = typer.Argument(..., help="Pack directory"),
):
    """Install a pack."""
    from nous_runtime.services.packs import install_pack

    result = install_pack(path)
    typer.echo(f"Pack installed: {result.get('name', path)}")


@pack_app.command("remove")
def pack_remove_cmd(
    name: str = typer.Argument(..., help="Pack name"),
):
    """Remove an installed pack."""
    from nous_runtime.services.packs import remove_pack

    remove_pack(name)
    typer.echo(f"Pack removed: {name}")




@capability_app.command("list")
def capability_list_cmd():
    """List registered capabilities."""
    from nous_runtime.services.capabilities import list_capabilities

    capabilities = list_capabilities()
    if not capabilities:
        typer.echo("No capabilities registered.")
        return
    for capability in capabilities:
        if isinstance(capability, dict):
            typer.echo(capability.get("name", "?"))
        else:
            typer.echo(str(capability))

def _print_json(data: object) -> None:
    typer.echo(json.dumps(data, indent=2))


def _current_workspace():
    from pathlib import Path
    from nous_runtime.project.workspace import find_workspace

    return find_workspace() or Path(".nous")


def _current_project_id(workspace) -> str:
    from pathlib import Path

    project_file = Path(workspace) / "project.json"
    if project_file.is_file():
        try:
            data = json.loads(project_file.read_text(encoding="utf-8"))
            return str(data.get("name") or Path(workspace).parent.name)
        except Exception:
            pass
    return Path(workspace).parent.name


@capability_app.command("availability")
def capability_availability_cmd(
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show capability availability."""
    from nous_runtime.capability.availability import check_availability

    result = check_availability()
    if json_output:
        _print_json(result)
        return
    typer.echo(f"Available: {len(result.get('available', []))}")
    typer.echo(f"Unavailable: {len(result.get('unavailable', []))}")


@inspect_app.callback(invoke_without_command=True)
def inspect_cmd(
    ctx: typer.Context,
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Inspect runtime snapshots."""
    if ctx.invoked_subcommand is not None:
        return
    from nous_runtime.inspector.snapshot import snapshot

    data = snapshot().to_dict()
    data.setdefault("counts", {
        "providers": len(data.get("providers", [])),
        "capabilities": len(data.get("capabilities", [])),
        "tasks": len(data.get("tasks", [])),
        "plans": len(data.get("plans", [])),
        "observations": len(data.get("observations", [])),
        "devices": len(data.get("devices", [])),
    })
    if json_output:
        _print_json(data)
    else:
        runtime = data.get("runtime", {})
        typer.echo(f"Runtime: {runtime.get('version', 'unknown')}")
        typer.echo(f"Providers: {runtime.get('providers', 0)}")
        typer.echo(f"Capabilities: {runtime.get('capabilities', 0)}")


@inspect_retrieval_app.callback(invoke_without_command=True)
def inspect_retrieval_cmd(
    ctx: typer.Context,
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Inspect retrieval state."""
    if ctx.invoked_subcommand is not None:
        return
    from nous_runtime.retrieval.inspector import retrieval_snapshot

    data = retrieval_snapshot(_current_workspace())
    if json_output:
        _print_json(data)
    else:
        typer.echo(f"Indexes: {len(data.get('indexes', []))}")
        typer.echo(f"Jobs: {len(data.get('jobs', []))}")


@retrieval_index_app.command("rebuild")
def retrieval_index_rebuild_cmd(
    workspace_id: str = typer.Option("workspace", "--workspace-id", help="Workspace ID"),
    project_id: str = typer.Option("", "--project-id", help="Project ID"),
    logical_index: str = typer.Option("memory", "--index", help="Logical index name"),
    backend_id: str = typer.Option("local", "--backend", help="Backend ID"),
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Rebuild a retrieval index generation."""
    from nous_runtime.retrieval import LogicalIndexSpec, RetrievalIndexManager

    workspace = _current_workspace()
    spec = LogicalIndexSpec(
        logical_index=logical_index,
        backend_id=backend_id,
        workspace_id=workspace_id,
        project_id=project_id or _current_project_id(workspace),
    )
    result = RetrievalIndexManager(workspace_path=workspace).rebuild(spec)
    data = {
        "generation_id": result.generation_id,
        "exported_records": result.exported_records,
        "indexed_records": result.indexed_records,
        "skipped_records": result.skipped_records,
        "failed_records": result.failed_records,
        "batch_count": result.batch_count,
        "duration_ms": result.duration_ms,
        "errors": list(result.errors),
        "ok": result.ok,
    }
    if json_output:
        _print_json(data)
    else:
        typer.echo(
            f"generation={result.generation_id} exported={result.exported_records} "
            f"indexed={result.indexed_records} failed={result.failed_records}"
        )


@retrieval_index_app.command("status")
def retrieval_index_status_cmd(
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show retrieval index generations."""
    from nous_runtime.retrieval import RetrievalIndexManager

    items = [item.to_dict() for item in RetrievalIndexManager(workspace_path=_current_workspace()).status()]
    if json_output:
        _print_json(items)
    else:
        if not items:
            typer.echo("No index generations.")
            return
        for item in items:
            typer.echo(f"{item.get('generation_id')} {item.get('state')} records={item.get('record_count')}")


@retrieval_index_app.command("verify")
def retrieval_index_verify_cmd(
    generation_id: str = typer.Argument(..., help="Generation ID"),
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Verify a retrieval index generation."""
    from nous_runtime.retrieval import RetrievalIndexManager

    result = RetrievalIndexManager(workspace_path=_current_workspace()).verify_generation(generation_id)
    data = result.to_dict()
    if json_output:
        _print_json(data)
    else:
        typer.echo(f"valid={result.valid} expected={result.expected_count} actual={result.actual_count}")


@provider_app.command("circuit")
def provider_circuit_cmd(
    action_or_provider: str = typer.Argument(..., help="Action or provider ID"),
    provider_id: str = typer.Argument("", help="Provider ID for open/close"),
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show or change provider circuit state."""
    import uuid
    from nous_runtime.intelligence.reliability import CircuitState, CircuitStateRecord, JsonlReliabilityStore

    store = JsonlReliabilityStore(_current_workspace())
    action = action_or_provider.lower()
    if action in {"open", "close"}:
        if not provider_id:
            typer.echo("provider_id is required", err=True)
            raise typer.Exit(code=2)
        state = CircuitState.FORCED_OPEN if action == "open" else CircuitState.CLOSED
        previous = CircuitState.CLOSED if action == "open" else CircuitState.FORCED_OPEN
        record = CircuitStateRecord(
            record_id=f"circuit_{uuid.uuid4().hex}",
            breaker_key=f"{provider_id}:*",
            state=state,
            previous_state=previous,
            transition_reason=f"cli.force_{action}",
        )
        store.append_circuit_event(record)
        data = record.to_dict()
    else:
        provider_id = action_or_provider
        record = store.get_circuit_state(f"{provider_id}:*")
        data = record.to_dict() if record else {"breaker_key": f"{provider_id}:*", "state": "closed"}
    if json_output:
        _print_json(data)
    else:
        typer.echo(data.get("state", "closed"))

provider_reliability_app = typer.Typer(help="Provider reliability diagnostics")
provider_app.add_typer(provider_reliability_app, name="reliability")


@provider_reliability_app.command("verify")
def provider_reliability_verify_cmd(
    json_output: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Verify provider reliability store."""
    from nous_runtime.intelligence.reliability import JsonlReliabilityStore

    result = JsonlReliabilityStore(_current_workspace()).verify_integrity()
    data = {**result, "canonical_wrapper": True}
    if json_output:
        _print_json(data)
    else:
        typer.echo("Provider reliability: OK" if data.get("ok") else "Provider reliability: FAILED")
# debug commands

@debug_app.command("providers")
def debug_providers_cmd():
    """Show full provider visibility across every layer."""
    from nous_runtime.cli.debug_providers import debug_providers
    from nous_runtime.cli.provider_setup import load_providers_from_config
    load_providers_from_config()
    typer.echo(debug_providers())


# Connectivity commands

server_app = typer.Typer(help="Control Plane server management")
app.add_typer(server_app, name="server")

node_app = typer.Typer(help="Node management")
app.add_typer(node_app, name="node")

task_app = typer.Typer(help="Task management")
app.add_typer(task_app, name="task")

project_app = typer.Typer(help="Project management")
app.add_typer(project_app, name="project")


@server_app.command("init")
def server_init_cmd(
    host: str = typer.Option("127.0.0.1", help="Bind host"),
    port: int = typer.Option(9770, help="Bind port"),
):
    """Initialize the Control Plane."""
    from nous_runtime.connectivity.cli.commands import server_init
    server_init(host, port)


@server_app.command("start")
def server_start_cmd():
    """Start the Control Plane."""
    from nous_runtime.connectivity.cli.commands import server_start
    server_start()


@server_app.command("status")
def server_status_cmd(
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show Control Plane status."""
    from nous_runtime.connectivity.cli.commands import server_status
    server_status(json_fmt)


@node_app.command("pair")
def node_pair_cmd():
    """Create a pairing code for a new node."""
    from nous_runtime.connectivity.cli.commands import node_pair
    node_pair()


@node_app.command("join")
def node_join_cmd(
    code: str = typer.Argument(..., help="Pairing code from 'nous node pair'"),
    name: str = typer.Option("node", help="Node name"),
    host: str = typer.Option("127.0.0.1", help="Control Plane host"),
    port: int = typer.Option(9770, help="Control Plane port"),
):
    """Join a Control Plane using a pairing code."""
    from nous_runtime.connectivity.cli.commands import node_join
    node_join(code, name, host, port)


@node_app.command("start")
def node_start_cmd(
    name: str = typer.Option("node", help="Node name"),
    host: str = typer.Option("127.0.0.1", help="Control Plane host"),
    port: int = typer.Option(9770, help="Control Plane port"),
):
    """Start the Node daemon."""
    from nous_runtime.connectivity.cli.commands import node_start
    node_start(name, host, port)


@node_app.command("status")
def node_status_cmd(
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show node status."""
    from nous_runtime.connectivity.cli.commands import node_status
    node_status(json_fmt)


@node_app.command("list")
def node_list_cmd(
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """List all paired nodes."""
    from nous_runtime.connectivity.cli.commands import node_list
    node_list(json_fmt)


@node_app.command("show")
def node_show_cmd(
    node_id: str = typer.Argument(..., help="Node ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show a specific node."""
    from nous_runtime.connectivity.cli.commands import node_show
    node_show(node_id, json_fmt)


@node_app.command("revoke")
def node_revoke_cmd(
    node_id: str = typer.Argument(..., help="Node ID to revoke"),
):
    """Revoke a node's credentials."""
    from nous_runtime.connectivity.cli.commands import node_revoke
    node_revoke(node_id)


@task_app.command("submit")
def task_submit_cmd(
    capability: str = typer.Argument(..., help="Capability ID (e.g., system.echo)"),
    message: str = typer.Option("", help="Message for system.echo"),
    target: str = typer.Option("", help="Target node ID"),
    deadline: str = typer.Option("", help="Task deadline (ISO-8601)"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Submit a task."""
    from nous_runtime.connectivity.cli.commands import task_submit
    task_submit(capability, message, target, deadline, json_fmt)


@task_app.command("list")
def task_list_cmd(
    state: str = typer.Option("", help="Filter by state"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """List tasks."""
    from nous_runtime.connectivity.cli.commands import task_list
    task_list(state, json_fmt)


@task_app.command("show")
def task_show_cmd(
    task_id: str = typer.Argument(..., help="Task ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show a specific task."""
    from nous_runtime.connectivity.cli.commands import task_show
    task_show(task_id, json_fmt)


@task_app.command("events")
def task_events_cmd(
    task_id: str = typer.Argument(..., help="Task ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show task events."""
    from nous_runtime.connectivity.cli.commands import task_events
    task_events(task_id, json_fmt)


@task_app.command("cancel")
def task_cancel_cmd(
    task_id: str = typer.Argument(..., help="Task ID to cancel"),
):
    """Cancel a task."""
    from nous_runtime.connectivity.cli.commands import task_cancel
    task_cancel(task_id)


# Project commands

@project_app.command("create")
def project_create_cmd(
    name: str = typer.Argument(..., help="Project name"),
    description: str = typer.Option("", help="Project description"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Create a new project."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    result = pc.create_project(name, description)
    if result:
        if json_fmt:
            typer.echo(json.dumps(result, indent=2))
        else:
            typer.echo(f"Project created: {result['project_id']}")
            typer.echo(f"  Name: {result['name']}")
            typer.echo(f"  Status: {result['status']}")
    else:
        typer.echo("Failed to create project.")


@project_app.command("list")
def project_list_cmd(
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """List all projects."""
    from nous_runtime.connectivity.project.store import ProjectStore
    projects = ProjectStore().list_projects()
    if json_fmt:
        typer.echo(json.dumps(projects, indent=2))
    else:
        if not projects:
            typer.echo("No projects.")
            return
        for p in projects:
            icon = {"active": "ACTIVE", "draft": "DRAFT", "paused": "PAUSED", "completed": "DONE", "cancelled": "CANCELLED"}.get(p.get("status", ""), "UNKNOWN")
            typer.echo(f"{icon} {p.get('project_id')} [{p.get('status')}] {p.get('name')}")


@project_app.command("show")
def project_show_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show project details."""
    from nous_runtime.connectivity.project.store import ProjectStore
    p = ProjectStore().get_project(project_id)
    if not p:
        typer.echo(f"Project '{project_id}' not found.")
        return
    if json_fmt:
        typer.echo(json.dumps(p, indent=2))
    else:
        for k, v in p.items():
            typer.echo(f"  {k}: {v}")


@project_app.command("start")
def project_start_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
):
    """Activate a project."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    if pc.activate(project_id):
        typer.echo(f"Project '{project_id}' activated.")
    else:
        typer.echo(f"Failed to activate project '{project_id}'.")


@project_app.command("continue")
def project_continue_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
):
    """Continue a project (deterministic resolution)."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    decision = pc.continue_project(project_id)
    typer.echo(f"Action: {decision.action}")
    typer.echo(f"Reason: {decision.reason}")
    if decision.resolved_work_item:
        typer.echo(f"WorkItem: {decision.resolved_work_item}")


@project_app.command("pause")
def project_pause_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
    reason: str = typer.Option("", help="Pause reason"),
):
    """Pause a project."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    if pc.pause(project_id, reason):
        typer.echo(f"Project '{project_id}' paused.")
    else:
        typer.echo(f"Failed to pause project '{project_id}'.")


@project_app.command("resume")
def project_resume_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
):
    """Resume a paused project."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    if pc.resume(project_id):
        typer.echo(f"Project '{project_id}' resumed.")
    else:
        typer.echo(f"Failed to resume project '{project_id}'.")


@project_app.command("cancel")
def project_cancel_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
):
    """Cancel a project."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    if pc.cancel_project(project_id):
        typer.echo(f"Project '{project_id}' cancelled.")
    else:
        typer.echo(f"Failed to cancel project '{project_id}'.")


@project_app.command("progress")
def project_progress_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show project progress."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    snap = pc.get_progress(project_id)
    if not snap:
        typer.echo(f"Project '{project_id}' not found.")
        return
    if json_fmt:
        typer.echo(json.dumps(snap.to_dict(), indent=2))
    else:
        typer.echo(f"Progress: {snap.progress_pct}% ({snap.completed}/{snap.total_work_items})")
        typer.echo(f"  Health: {snap.health}")
        typer.echo(f"  Next: {snap.next_action}")
        if snap.requires_user_action:
            typer.echo("  Requires user action.")


@project_app.command("checkpoints")
def project_checkpoints_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """List project checkpoints."""
    from nous_runtime.connectivity.project.store import ProjectStore
    checkpoints = ProjectStore().list_checkpoints(project_id)
    if json_fmt:
        typer.echo(json.dumps(checkpoints, indent=2))
    else:
        if not checkpoints:
            typer.echo("No checkpoints.")
            return
        for cp in checkpoints:
            typer.echo(f"  [{cp.get('created_at')}] {cp.get('description')}")


@project_app.command("events")
def project_events_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """List project events."""
    from nous_runtime.connectivity.project.coordinator import ProjectCoordinator
    pc = ProjectCoordinator()
    events = pc.get_events(project_id)
    if json_fmt:
        typer.echo(json.dumps(events, indent=2))
    else:
        if not events:
            typer.echo("No events.")
            return
        for e in events:
            typer.echo(f"  [{e.get('created_at')}] {e.get('event_type')} {e.get('work_item_id', '')}")


@project_app.command("plan")
def project_plan_cmd(
    project_id: str = typer.Argument(..., help="Project ID"),
    json_fmt: bool = typer.Option(False, "--json", help="JSON output"),
):
    """Show project plan."""
    from nous_runtime.connectivity.project.store import ProjectStore
    plan = ProjectStore().get_plan(project_id)
    items = ProjectStore().list_work_items(project_id)
    if json_fmt:
        typer.echo(json.dumps({"plan": plan, "work_items": items}, indent=2))
    else:
        if plan:
            typer.echo(f"Plan: {plan['plan_id']} v{plan.get('version', 1)}")
        if not items:
            typer.echo("No work items.")
            return
        for wi in items:
            icon = {"succeeded": "DONE", "failed": "FAIL", "running": "RUN", "ready": "READY",
                    "planned": "PLAN", "blocked": "BLOCKED"}.get(wi.get("status", ""), "UNKNOWN")
            typer.echo(f"  {icon} {wi.get('work_item_id')} [{wi.get('status')}] {wi.get('description')}")


if __name__ == "__main__":
    # B1 Governance CLI
    try:
        from nous_runtime.governance.cli import approval_app, authorization_app, delegation_app
        app.add_typer(approval_app, name="approval")
        app.add_typer(authorization_app, name="authorization")
        app.add_typer(delegation_app, name="delegation")
    except Exception:
        pass
    app()
