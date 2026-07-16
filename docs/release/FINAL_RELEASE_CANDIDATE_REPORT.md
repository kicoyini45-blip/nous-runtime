# Final Release Candidate Report

Classification: **RELEASE_CANDIDATE_READY**

Version target: `v0.1.0-alpha`
Validation date: 2026-07-17
Validated source: exact manifest-generated `F:\Nous_Public` tree
Feature state: PRODUCT FEATURE_FREEZE

## Decision

The Sprint 20 public candidate is synchronized and release-candidate ready. The public tree contains exactly the 736 approved INCLUDE files, includes the service-first Provider Wizard, `/provider quick`, `/provider doctor`, Provider documentation and terminal completion updates, and contains no Git metadata or private/internal Runtime material. No Git initialization, staging, commit, push, tag or publication occurred.

## Sprint 20 synchronization

- Public tree regenerated from 736 INCLUDE entries in `PUBLIC_SOURCE_MANIFEST.md`.
- Path-set result: 0 missing, 0 unexpected, 0 duplicate and 0 hash-mismatched files.
- Sprint 20 source, tests and public documentation match `F:\Agent_play` byte-for-byte.
- `docs/review/UPGRADE_EXECUTION_LEDGER.md`, unsupported `remote_terminal/agent.py`, Android, `.git`, `.nous`, caches, databases, JSONL state, build output and egg metadata remain excluded.
- Focused public-tree validation: 119 Provider, Terminal and Governance/boundary tests passed under warning-as-error; affected Ruff and compilation passed.

## Provider product verification

| Check | Result |
| --- | --- |
| `/provider add` | PASS using installed Python 3.11 wheel and a local OpenAI-compatible service |
| `/provider quick` | PASS; entered credential remained process-scoped and was not persisted or printed |
| `/provider doctor` | PASS for healthy and unreachable Providers |
| OpenAI preset | PASS; service mapping and official base endpoint verified |
| DeepSeek preset | PASS; OpenAI-compatible mapping and current base endpoint verified |
| Ollama preset | PASS; local endpoint and `/api/tags` model discovery verified |
| Model discovery/selection | PASS; catalog discovery and interactive selection exercised |
| Error guidance | PASS; unreachable Provider rendered `Needs attention` with bounded status detail |
| Local restart | PASS; saved Provider configuration reloaded and Doctor returned healthy |
| Real external Provider E2E | SKIPPED; no supported maintainer credential environment variable was available. OS secret stores were not enumerated and no paid external request was sent. |

The conditional external flow `setup -> doctor -> model selection -> streamed conversation -> restart` is therefore not claimed as executed. This is non-blocking because the task required it only when maintainer credentials were available.

## Final release gate

| Gate | Result | Evidence |
| --- | --- | --- |
| Manifest boundary | PASS | 736 INCLUDE, 229 EXCLUDE, 263 PRIVATE_ONLY; 0 unresolved decisions |
| Public-tree integrity | PASS | 736 exact files; 0 missing, unexpected, forbidden or hash-mismatched files |
| Ruff | PASS | `python -m ruff check .` returned no findings |
| Compilation | PASS | `nous_runtime` and `remote_terminal.nous_core` compiled |
| Collection | PASS | 1330 tests collected |
| Serial tests | PASS | 1330 passed under warning-as-error in 523.08 seconds |
| Parallel tests | PASS | 1330 passed with pytest-xdist in 326.15 seconds |
| Build | PASS | wheel and sdist built in Python 3.11 |
| Package inspection | PASS | wheel 475 entries; sdist 620 entries; required Runtime files present; forbidden entries 0 |
| Clean installs | PASS | fresh Python 3.11 minimal and UI installations |
| Installed CLI/TUI | PASS | version, Provider help, Slash completion, non-TTY TUI and compatibility-kernel imports |
| Installed Server/Node | PASS | empty-state commands and authenticated random-port localhost HTTP smoke |
| Security/hygiene | PASS | HIGH 0; 10 MEDIUM classified; 15 hygiene/security tests passed |
| Targeted soak | PASS | 30.566 seconds; 49/49; 0 errors, crashes or corruption; no detected memory leak; 3 SQLite integrity checks passed |
| Android | EXCLUDED | Experimental/Unverified and outside the Alpha release gate |

## Security classification

The automated scanner reported 0 HIGH and 10 MEDIUM matches. Four are explicit `change-me` deployment placeholders. Four are protocol, enum or credential-reference identifiers. One is a synthetic Unix path in a test, and one is a synthetic bearer value in the Provider redaction test. No real credential, private key, personal repository path, private Runtime state or conversation content was found.

## Artifact identity

- Wheel: `nous_runtime-0.1.0a0-py3-none-any.whl`
- Wheel SHA-256: `0C5F2105E4654D5E911FBFC764129ABE1203050D7C0623EE57FBBD313AD5AA39`
- Sdist: `nous_runtime-0.1.0a0.tar.gz`
- Sdist SHA-256: `ABC425ADC080248506F9945AF7041F7CF040208AC08F2D80C0B76910E4E0846D`

## Performance comparison

| Benchmark | Previous public reference | Sprint 20 final | Assessment |
| --- | ---: | ---: | --- |
| Startup cold | 3.425s | 3.646s | PASS; below 5s target |
| Startup warm | 1.195s | 1.131s | PASS; below 2s target |
| Daemon recovery | 0.867s | 0.852s | PASS; below 5s target |
| Scheduler p95, 100 candidates | 15.075ms | 18.336ms | PASS; below 100ms target |
| Retrieval p95, 1000 records | 21.928ms | 22.750ms | PASS; below 100ms target |

Sprint 20 did not modify Runtime algorithms, state ownership, schemas, Governance or scheduling semantics.

## Maintainer-controlled actions

The exact public tree is ready for the separately authorized clean Git import. Git initialization, identity configuration, explicit staging, staged-diff review, commit, repository creation, remote configuration, tag, push, artifact upload and release publication remain unauthorized.
