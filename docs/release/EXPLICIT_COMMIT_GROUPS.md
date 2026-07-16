# Explicit Commit Groups

These commands are for the future clean public repository only. Run them after explicit maintainer approval. Never use `git add .`.

## Group 1 — Legal, identity, and project metadata

```powershell
git add -- .env.example .gitignore API_COMPATIBILITY.md CHANGELOG.md CODE_OF_CONDUCT.md config.example.json CONTRIBUTING.md LICENSE MAINTAINERS.md MANIFEST.in NOTICE README.md README.zh-CN.md ROADMAP.md SECURITY.md SUPPORT.md pyproject.toml nous_light.svg
```

## Group 2 — Runtime source and compatibility kernel

```powershell
git add -- nous_runtime remote_terminal/nous_core
```

## Group 3 — Product clients, SDK examples, and extension examples

```powershell
git add -- desktop ide examples hello_pack packs
```

## Group 4 — Deployment and operations

```powershell
git add -- deploy deploy.sh docker-compose.yml Dockerfile install.sh scripts/healthcheck.sh scripts/nous-doctor.sh scripts/validate_clean_install.ps1 scripts/validate_clean_install.sh
```

## Group 5 — Deterministic validation and performance tools

```powershell
git add -- tests scripts/security_scan.py scripts/smoke_test_clean_install.py scripts/benchmark scripts/benchmark_scheduler.py scripts/soak
```

## Group 6 — Public documentation and community templates

```powershell
git add -- .github docs
```

After each group:

```powershell
git diff --cached --name-status
git diff --cached --check
git diff --cached
```

Before committing, compare the staged file list with the 736 INCLUDE rows in `docs/release/PUBLIC_SOURCE_MANIFEST.md`. If an unexpected path appears:

```powershell
git restore --staged -- '<UNEXPECTED_PATH>'
```
