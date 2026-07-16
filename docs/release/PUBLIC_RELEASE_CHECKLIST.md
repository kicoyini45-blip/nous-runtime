# Public Release Checklist

Status: **RELEASE_CANDIDATE_READY - AWAITING GIT AUTHORIZATION**

## Source boundary

- [x] Regenerate `F:\Nous_Public` from the 736 approved INCLUDE entries.
- [x] Confirm 736 files, 0 missing, 0 unexpected, 0 duplicate and 0 hash mismatches.
- [x] Include the latest Provider Wizard, quick setup, Doctor, terminal completion, focused tests and public Provider documentation.
- [x] Exclude Git/private state, caches, build output, virtual environments, local configuration, Runtime JSONL/SQLite state, PRIVATE_ONLY and EXCLUDE files.
- [x] Exclude internal execution ledger, unsupported top-level Remote Terminal and Android.
- [x] Retain LICENSE, NOTICE, project metadata and `remote_terminal.nous_core`.

## Sprint 20 Provider validation

- [x] Focused public-tree Ruff and compilation.
- [x] Provider/Terminal/Governance validation: 119 passed under warning-as-error.
- [x] `/provider add` against a local OpenAI-compatible service.
- [x] `/provider quick` with process-scoped, non-persisted secret input.
- [x] `/provider doctor` healthy and failure guidance.
- [x] OpenAI, DeepSeek and Ollama preset verification.
- [x] Model catalog discovery and model selection.
- [x] Secret redaction in configuration and terminal output.
- [x] Saved Provider reload and post-restart Doctor.
- [ ] Real external Provider E2E: skipped because no maintainer credential environment variable was available; no external request was sent.

## Final validation

- [x] Ruff and supported-source compilation.
- [x] Collection: 1330 tests.
- [x] Warning-as-error suite: 1330 passed in 523.08 seconds.
- [x] Parallel suite: 1330 passed in 326.15 seconds.
- [x] Python 3.11 wheel and sdist build.
- [x] Package inspection: wheel 475 entries; sdist 620 entries; forbidden entries 0.
- [x] Clean Python 3.11 minimal and UI installations.
- [x] Installed CLI, Provider help, non-TTY TUI, Server/Node and localhost HTTP authentication smokes.
- [x] Security scan: HIGH 0; 10 MEDIUM classified as placeholders, identifiers or synthetic tests.
- [x] Security/hygiene tests: 15 passed.
- [x] Targeted soak: 49/49 in 30.566 seconds; 0 errors, crashes or corruption; no detected memory leak.
- [x] SQLite integrity: 3/3 databases reported `ok`.
- [x] Startup, Scheduler and Retrieval benchmarks remain within release targets.
- [x] Android remains Experimental/Unverified and outside the Alpha gate.

## Artifact identity

- [x] Wheel: `nous_runtime-0.1.0a0-py3-none-any.whl`
- [x] Wheel SHA-256: `0C5F2105E4654D5E911FBFC764129ABE1203050D7C0623EE57FBBD313AD5AA39`
- [x] Sdist: `nous_runtime-0.1.0a0.tar.gz`
- [x] Sdist SHA-256: `ABC425ADC080248506F9945AF7041F7CF040208AC08F2D80C0B76910E4E0846D`

## Maintainer approvals required

- [ ] Approve Git initialization and maintainer email configuration.
- [ ] Approve each explicit staging group; never use `git add .`.
- [ ] Review `git diff --cached --check`, staged names and full staged diff.
- [ ] Approve the clean import commit.
- [ ] Approve creation of `kicoyini45-blip/nous-runtime` without imported history.
- [ ] Approve annotated tag `v0.1.0-alpha`.
- [ ] Approve branch and tag pushes.
- [ ] Approve wheel/sdist attachment and GitHub pre-release publication.

No Git initialization, staging, commit, push, tag, remote creation or publication has occurred.
