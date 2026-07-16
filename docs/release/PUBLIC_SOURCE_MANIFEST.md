# Public Source Manifest

Status: VALIDATED PUBLIC SOURCE BOUNDARY

This manifest covers every tracked or untracked, non-ignored repository file visible at generation time. It does not authorize copying, staging, committing, or publication.

## Mandatory path exclusions

Always exclude .git, .nous, virtual environments, caches, build, dist, egg metadata, databases, SQLite files, JSONL Runtime state, local configuration, private server addresses, credentials, conversation logs, temporary audit material, internal execution records, and development-assistant attribution.

## Blocker-closure decision groups

The former 356 REWRITE entries were resolved as explicit release groups:

- INCLUDE: distributed Nous Runtime compatibility modules and remote_terminal.nous_core.
- EXCLUDE: the Experimental/Unverified Android client and unverified or duplicate legacy public documentation.
- PRIVATE_ONLY: the unsupported top-level remote_terminal application and internal or obsolete development-phase records.
- LEGAL_REVIEW: resolved for LICENSE; the Apache-2.0 text is retained intact and matches project metadata.

No REWRITE or LEGAL_REVIEW entry remains eligible for or unresolved in the public copy.
## Decisions

| Path | Decision | Document or file class | Rationale |
| --- | --- | --- | --- |
| .env.example | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| .github/ISSUE_TEMPLATE/bug_report.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| .github/ISSUE_TEMPLATE/feature_request.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| .github/PULL_REQUEST_TEMPLATE.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| .gitignore | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| API_COMPATIBILITY.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| CHANGELOG.md | INCLUDE | RELEASE | Public RELEASE candidate; retain after final staged review. |
| CLEAN_ROOM_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal clean-room working report; do not publish. |
| CODE_OF_CONDUCT.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| config.example.json | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| CONTRIBUTING.md | INCLUDE | DEVELOPER_DOCUMENTATION | Public DEVELOPER_DOCUMENTATION candidate; retain after final staged review. |
| deploy.sh | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| deploy/brew/nous-runtime.rb | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| deploy/docker/docker-compose.yml | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| deploy/nousd.service | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| deploy/windows/install.ps1 | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| desktop/index.html | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| desktop/package.json | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| desktop/README.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| desktop/src/App.tsx | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| desktop/src/lib/api.ts | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| desktop/src/main.tsx | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| desktop/src-tauri/build.rs | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| desktop/src-tauri/Cargo.toml | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| desktop/src-tauri/src/main.rs | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| desktop/src-tauri/tauri.conf.json | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| desktop/tsconfig.json | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| desktop/vite.config.ts | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| docker-compose.yml | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| Dockerfile | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| docs/architecture/ARCHITECTURE.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/CAPABILITY_CONTRACT.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/CLI_ARCHITECTURE.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/COMPATIBILITY_POLICY.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/CONTROL_CENTER_ALIGNMENT.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/CONTROL_CENTER_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/DISTRIBUTION.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/ERROR_MODEL.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/EXECUTION_CONTRACT.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/GLOSSARY.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/KERNEL_ARCHITECTURE_V1.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/KERNEL_MODULE_MAP.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/LAYERS.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/LEARNING_DOMAIN_MIGRATION.md | PRIVATE_ONLY | ARCHITECTURE | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/architecture/MOBILE_RUNTIME_INTEGRATION.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/MULTI_AGENT_ORCHESTRATION.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/OBJECT_MODEL.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/PACK_SPEC_V1.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/PROVIDER_CONTRACT.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/README.md | INCLUDE | ARCHITECTURE | Public ARCHITECTURE candidate; retain after final staged review. |
| docs/architecture/REGISTRY_CONTRACT.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/REGISTRY_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/RUNTIME_BOUNDARY.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/SECURITY_CONTRACT.md | EXCLUDE | SECURITY | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/SECURITY_HARDENING.md | EXCLUDE | SECURITY | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/architecture/V1.2.0_PLAN.md | PRIVATE_ONLY | ARCHITECTURE | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/BRAND_IDENTITY.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/CAPABILITY_AVAILABILITY.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/community/BETA_TEST_TEMPLATE.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/community/GOVERNANCE.md | EXCLUDE | GOVERNANCE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/community/MAINTAINERS.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/deployment/DEPLOYMENT.md | EXCLUDE | OPERATIONS | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/deployment/README.md | INCLUDE | OPERATIONS | Public OPERATIONS candidate; retain after final staged review. |
| docs/design/PACK_MODEL.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/design/PRODUCT_IDENTITY.md | INCLUDE | ARCHITECTURE | Public ARCHITECTURE candidate; retain after final staged review. |
| docs/design/SOFTWARE_DESIGN.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/design/TUI_DESIGN_LANGUAGE.md | INCLUDE | ARCHITECTURE | Public ARCHITECTURE candidate; retain after final staged review. |
| docs/design/VOICE_AND_TONE.md | INCLUDE | ARCHITECTURE | Public ARCHITECTURE candidate; retain after final staged review. |
| docs/developer/API_REFERENCE.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/CLI_REFERENCE.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/ECOSYSTEM.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/GETTING_STARTED.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/PACK_DEVELOPMENT.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/PROVIDER_DEVELOPMENT.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/QUICKSTART.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/README.md | INCLUDE | DEVELOPER_DOCUMENTATION | Public DEVELOPER_DOCUMENTATION candidate; retain after final staged review. |
| docs/developer/WRITE_A_MODULE.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/developer/WRITE_A_PROVIDER.md | EXCLUDE | DEVELOPER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/FIRST_RUN.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/getting_started/FIRST_RUN.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/getting_started/INSTALL_DOCKER.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/getting_started/INSTALL_LINUX.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/getting_started/INSTALL_MACOS.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/getting_started/INSTALL_WINDOWS.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/getting_started/TROUBLESHOOTING.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/getting-started/README.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| docs/guides/ARCHITECTURE_OVERVIEW.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/guides/CLI_GUIDE.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/guides/DEPLOYMENT_GUIDE.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/guides/PACK_GUIDE.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/guides/PROVIDER_GUIDE.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/guides/README.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| docs/guides/USER_GUIDE.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/INSTALLATION.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/intelligence/EXECUTION_MODEL.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/intelligence/PLANNER.md | PRIVATE_ONLY | USER_DOCUMENTATION | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/intelligence/PROVIDER_ROUTING.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/LOCAL_MEMORY.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/OBSERVATION_LAYER.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/operations/BACKUP_RESTORE.md | EXCLUDE | OPERATIONS | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/operations/NODE_DEPLOYMENT.md | EXCLUDE | OPERATIONS | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/operations/REMOTE_ACCESS.md | EXCLUDE | OPERATIONS | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/operations/SERVER_DEPLOYMENT.md | EXCLUDE | OPERATIONS | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/p0/current_architecture.md | PRIVATE_ONLY | OBSOLETE | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/p0/deploy_guide.md | PRIVATE_ONLY | OBSOLETE | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/p0/integration_points.md | PRIVATE_ONLY | OBSOLETE | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/p0/risk_report.md | PRIVATE_ONLY | OBSOLETE | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/p1/failure_recovery_report.md | PRIVATE_ONLY | USER_DOCUMENTATION | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/p1/kernel_health_report.md | PRIVATE_ONLY | USER_DOCUMENTATION | Internal or obsolete development-phase record; not part of public product documentation. |
| docs/PROJECT.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/PROJECT_RUNTIME.md | EXCLUDE | USER_DOCUMENTATION | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/protocol/ESP32_SDK.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/protocol/MESSAGE_ENVELOPE.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/protocol/NEP_SPEC.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/protocol/NFP_SPEC.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/protocol/NKP_SPEC.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/protocol/NOUS_PROTOCOL_OVERVIEW.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/protocol/NSP_SPEC.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/release/ALPHA_SCOPE.md | INCLUDE | RELEASE | Public RELEASE candidate; retain after final staged review. |
| docs/release/CLEAN_PUBLIC_IMPORT_PLAN.md | PRIVATE_ONLY | RELEASE | Internal clean-import execution plan; do not publish. |
| docs/release/CODE_CLEAN_PASS_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/CONVERSATION_PERFORMANCE_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/EXPLICIT_COMMIT_GROUPS.md | INCLUDE | RELEASE | Public RELEASE candidate; retain after final staged review. |
| docs/release/FINAL_ALPHA_INTEGRATION_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/FINAL_RELEASE_CANDIDATE_REPORT.md | INCLUDE | RELEASE | Public RELEASE candidate; retain after final staged review. |
| docs/release/GIT_HISTORY_REVIEW.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/KNOWN_LIMITATIONS.md | INCLUDE | RELEASE | Public RELEASE candidate; retain after final staged review. |
| docs/release/LEGACY_MOBILE_CLIENT_AUDIT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/MOBILE_AND_MULTI_AGENT_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/NOUS_ALPHA_ARCHITECTURE_STATUS.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/OPEN_SOURCE_READINESS_AUDIT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/OPEN_SOURCE_REVIEW.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/performance/database.json | EXCLUDE | CONFIGURATION | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| docs/release/performance/model_runtime.json | EXCLUDE | CONFIGURATION | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| docs/release/performance/resource.json | EXCLUDE | CONFIGURATION | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| docs/release/performance/scheduler.json | EXCLUDE | CONFIGURATION | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| docs/release/performance/soak_short.json | EXCLUDE | CONFIGURATION | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| docs/release/performance/startup.json | EXCLUDE | CONFIGURATION | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| docs/release/performance/test_suite.json | EXCLUDE | CONFIGURATION | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| docs/release/PHASE_10_CLIENT_INTEGRATION_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/PHASE_10_TERMINAL_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/PHASE_11_KNOWLEDGE_LIBRARY_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/PHASE_9_OPEN_SOURCE_PREPARATION_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/PHASE_9_PERFORMANCE_BASELINE.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/PHASE_9_SECURITY_TRIAGE.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/PUBLIC_EXPORT_MANIFEST.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/PUBLIC_RELEASE_CHECKLIST.md | INCLUDE | RELEASE | Public RELEASE candidate; retain after final staged review. |
| docs/release/PUBLIC_SOURCE_MANIFEST.md | INCLUDE | RELEASE | Public RELEASE candidate; retain after final staged review. |
| docs/release/RC_ALGORITHM_AND_PERFORMANCE_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/RC_ARCHITECTURE_REVIEW.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/RC_BASELINE_VERIFICATION.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/RC_DEFECT_REGISTER.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/RELEASE_CHECKLIST.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/RELEASE_RUNBOOK.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/RUNTIME_RESOURCE_PROFILE.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/SENSITIVE_SCAN_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/SOAK_TEST_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/TEST_INFRASTRUCTURE_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/V0.1.0_ALPHA_RELEASE_NOTES.md | INCLUDE | RELEASE | Public release notes for v0.1.0-alpha. |
| docs/release/V1_ALPHA_SELF_TEST_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/V1_FINAL_RELEASE_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/V1_OPEN_SOURCE_REPORT.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/release/V1_RELEASE_NOTES.md | PRIVATE_ONLY | RELEASE | Internal execution, handoff, audit, or release-working material. |
| docs/RELEASE_CHECKLIST.md | EXCLUDE | RELEASE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/review/AGENT_NETWORK_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/AGENT_RUNTIME_ARCHITECTURE_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/AGENT_RUNTIME_KNOWN_LIMITATIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/AGENT_RUNTIME_SECURITY_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/AGENT_RUNTIME_TEST_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/ARCHITECTURE_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/ARTIFACT_POLICY.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_0_SECURITY_HOTFIX_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_AUDIT_CONCLUSIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_AUTHORIZATION_GAP_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_BASELINE_VERIFICATION.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_EXECUTION_PATH_INVENTORY.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_GATE_EXPANSION_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_GATE_INTEGRATION_MATRIX.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_GOVERNANCE_STATE_OWNERSHIP.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_IMPLEMENTATION_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_IMPLEMENTATION_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_IMPLICIT_TRUST_RISK_REGISTER.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_KNOWN_LIMITATIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_API_AUTHORIZATION_MATRIX.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_BASELINE_VERIFICATION.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_CHAT_AUTH_VERIFICATION.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_CONTRACT_CONFORMANCE_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_DEPENDENCY_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_ENVELOPE_VERIFICATION.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_FAULT_INJECTION_VERIFICATION.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_MASTER_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_ROUND2_ENFORCEMENT_CLOSURE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_SCOPE_MATCHING_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_SECURITY_DELTA_TRIAGE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_R_STATE_OWNERSHIP_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_RELEASE_GATE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_RELEASE_GATE_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_SECURITY_RESULTS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/B1_TEST_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/COMPATIBILITY_MATRIX.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONNECTIVITY_EXISTING_SYSTEM_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONNECTIVITY_IMPLEMENTATION_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONNECTIVITY_RISK_REGISTER.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONTEXT_DATA_FLOW_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONTEXT_GAP_ANALYSIS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONTEXT_KNOWN_LIMITATIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONTEXT_PERFORMANCE_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONTEXT_RUNTIME_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/CONTEXT_SECURITY_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/DEPLOYMENT_GAP_ANALYSIS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/DEPRECATION_POLICY.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EVALUATION_DATA_FLOW.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EVALUATION_GAP_ANALYSIS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EVALUATION_LIMITATIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EVALUATION_PERFORMANCE_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EVALUATION_RUNTIME_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EVALUATION_SECURITY_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EXPERIENCE_DATA_FLOW.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EXPERIENCE_GAP_ANALYSIS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/EXPERIENCE_RUNTIME_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_A2_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_A3_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_A4_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_A5_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_A6_WORKTREE_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_COMMIT_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/FOUNDATION_HARDENING_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/GIT_HISTORY_REVIEW.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/KNOWN_LIMITATIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/LEGACY_COMPATIBILITY_SPEC.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/LEGACY_REUSE_MATRIX.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/MIGRATION_GUIDE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_2_0_COMPETITIVE_POSITION.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_2X_BASELINE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_CAPABILITY_GRAPH_DESIGN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_COMPETITIVE_ANALYSIS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_DEPENDENCY_GRAPH_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_EVALUATION_ENGINE_DESIGN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_INTELLIGENCE_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_INTELLIGENCE_EVOLUTION_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_MEMORY_EVOLUTION_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_ROADMAP_UPGRADE_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_RUNTIME_2_0_MASTER_ROADMAP.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_RUNTIME_ARCHITECTURE_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_RUNTIME_MODULE_MAP.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_SECURITY_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_SERVER_RUNTIME_ARCHITECTURE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_STATE_OWNERSHIP_MODEL.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/NOU_ZERO_TRUST_RUNTIME_MODEL.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/OPEN_SOURCE_REVIEW_V1.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/OPERATIONS_MODEL.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P3_INSPECTOR_BASELINE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P3_MEMORY_BASELINE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P3_OPEN_SOURCE_CLEAN_PASS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P4_RETRIEVAL_BASELINE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P4_RETRIEVAL_PIPELINE_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P4_RETRIEVAL_PRODUCTIONIZATION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_0_2_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_3_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_3_LIFECYCLE_GAP_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_4_1_STORE_CONCURRENCY_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_4_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_5_1_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_5_1_SCHEDULER_PERFORMANCE_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_5_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_5_SCHEDULING_GAP_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_6_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_6_MODEL_PROVIDER_GAP_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_7_1_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_7_1_INTEGRATION_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_7_2_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_7_2_EXECUTION_CLOSURE_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_7_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_7_RELIABILITY_GAP_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_8_PREPARATION_NOTES.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_BASELINE_CONTRACT_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_RUNTIME_INTELLIGENCE_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_SECURITY_FINDINGS_TRIAGE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_SYSTEM_INTEGRATION_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_SYSTEM_RISK_REGISTER.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/P5_SYSTEM_TRACEABILITY_MATRIX.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PACK_TRUST_MODEL.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PACKAGE_INSTALL_VALIDATION.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_0_5_ARCHITECTURE_DECISIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_0_5_IMPLEMENTATION_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_0_5_OPERATING_MODEL_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_0_5_SECURITY_BASELINE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_1_1_PACKAGING_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_1_1_PROCESS_BOUNDARY_TEST.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_1_1_TRACEABILITY_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_1_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_1_CONNECTIVITY_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_1_KNOWN_LIMITATIONS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_1_SECURITY_RESULTS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_2_AGENT_RUNTIME_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_3_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_3_CONTEXT_RUNTIME_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_4_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_5_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_8_ARCHITECTURE_PLAN.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_8_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_8_DEPENDENCY_MAP.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_8_RELEASE_GATE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_8_RUNTIME_FLOW_SPEC.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PHASE_COMPLETION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PRODUCT_IDENTITY_CHANGELOG.md | INCLUDE | RELEASE | Public product-identity change record; retain after final staged review. |
| docs/review/PRODUCTION_RUNTIME_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/PUBLIC_API_V1.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/REALITY_AUDIT_V1.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/RELEASE_PROCESS.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/RELEASE_STABILIZATION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/RELEASE_VALIDATION_FIX_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/RELEASE_VALIDATION_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/RUNTIME_PROTOCOL_AUDIT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/SECURITY_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/SUPPLY_CHAIN_SECURITY.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/TEST_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/THREAT_MODEL.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/UPGRADE_EXECUTION_LEDGER.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/V1_BASELINE_REPORT.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/review/V1_RELEASE_GATE.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| docs/security/ABUSE_CASES.md | EXCLUDE | SECURITY | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/security/README.md | INCLUDE | SECURITY | Public SECURITY candidate; retain after final staged review. |
| docs/security/SECURITY_CHECKLIST.md | EXCLUDE | SECURITY | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/security/THREAT_MODEL.md | EXCLUDE | SECURITY | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/security/TRUST_BOUNDARIES.md | EXCLUDE | SECURITY | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/ACCESS_CLIENT_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/ACTION_PROPOSAL_BINDING_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/APPROVAL_PROTOCOL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/APPROVAL_SCOPE_MATCHING_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/AUTHORIZATION_ACTION_MODE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/AUTHORIZATION_LIFECYCLE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/AUTHORIZATION_MODEL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/BENCHMARK_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CANDIDATE_MODEL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CAPABILITY_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CIRCUIT_BREAKER_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CONTEXT_MODEL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CONTEXT_PERMISSION_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CONTEXT_PROVIDER_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CONTEXT_RUNTIME_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/CONTINUATION_PROTOCOL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/DECISION_LIFECYCLE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/DECISION_OUTCOME_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/DECISION_SCORING_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/DECISION_STORE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/DELEGATION_ENFORCEMENT_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/DELEGATION_MODEL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/DEVICE_CREDENTIAL_LIFECYCLE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/EVALUATION_MODEL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/EVALUATION_RUNTIME_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/EXECUTION_AUTHORIZATION_GATE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/EXPERIENCE_LEARNING_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/EXPERIENCE_MODEL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/EXPERIENCE_RUNTIME_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/FAILURE_CLASSIFICATION_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/FEDERATION_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/GOVERNANCE_CLI_SPEC.md | EXCLUDE | GOVERNANCE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/GOVERNANCE_GLOSSARY.md | EXCLUDE | GOVERNANCE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/GOVERNANCE_RUNTIME_MODE_SPEC.md | EXCLUDE | GOVERNANCE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/GOVERNANCE_STORE_SPEC.md | EXCLUDE | GOVERNANCE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/LONG_RUNNING_PROJECT_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/MODEL_PROFILE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/MODULE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/NODE_IDENTITY_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/OPEN_RUNTIME_STANDARD.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/POLICY_OPTIMIZATION_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/POLICY_RUNTIME_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/PROFILE_STORE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/PROVIDER_PROFILE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/PUBLIC_NETWORK_SECURITY_SPEC.md | EXCLUDE | SECURITY | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/QUALITY_SCORING_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/RELAY_PROTOCOL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/RETRIEVAL_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/RETRY_POLICY_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/RISK_ASSESSMENT_ALGORITHM_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/RISK_ENVELOPE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/RUNTIME_CONSTITUTION_ENFORCEMENT_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/RUNTIME_INTELLIGENCE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/SCHEDULING_ENGINE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/SELF_DEVELOPMENT_PIPELINE_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/TASK_DELIVERY_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/UPDATE_AND_ROLLBACK_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/specs/WORKSPACE_RUNTIME_SPEC.md | EXCLUDE | ARCHITECTURE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| docs/standards/README.md | INCLUDE | ARCHITECTURE | Public ARCHITECTURE candidate; retain after final staged review. |
| docs/TERMINAL_EXPERIENCE.md | EXCLUDE | OBSOLETE | Unverified or duplicate legacy documentation; not selected for the v0.1.0-alpha public documentation set. |
| examples/demo_edge_device.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| examples/demo_quick_capture.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| examples/hello_provider/README.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| HANDOFF.md | PRIVATE_ONLY | PRIVATE_INTERNAL | Internal execution, handoff, audit, or release-working material. |
| hello_pack/pack.yaml | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| hello_pack/README.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| hello_pack/src/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| hello_pack/src/providers.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| hello_pack/tests/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| hello_pack/tests/test_providers.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| install.sh | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| LICENSE | INCLUDE | LEGAL | Apache-2.0 license text matches project metadata; retain intact in the public source set. |
| MANIFEST.in | INCLUDE | CONFIGURATION | Explicitly limits the sdist to supported Runtime and compatibility-kernel sources. |
| MAINTAINERS.md | INCLUDE | DEVELOPER_DOCUMENTATION | Public DEVELOPER_DOCUMENTATION candidate; retain after final staged review. |
| nous_light.svg | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/budget.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/executor.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/health.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/identity.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/lifecycle.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/manifest.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/orchestration.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/policy.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agent/sandbox.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/artifact_collector.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/command_adapter.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/environment_filter.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/event_parser.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/output_limiter.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/policy_evaluator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/supervisor.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/adapters/workspace_guard.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/external/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/agents/external/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/api/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/api/routes.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/api/server.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/backup/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/backup/manager.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/backup/recovery.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/capability/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/capability/availability.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/capability/lifecycle.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/capability/manifest.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/capability/resolver.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/chat/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/chat/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/chat/router.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/chat/runtime.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/debug_providers.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/decision.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/dev_commands.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/doctor.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/history.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/intelligence.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/main.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/policy.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/profiles.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/provider_setup.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/shell.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/shell_v2.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/stream.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/terminal_session.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/terminal_ui.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/utils.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/cli/wizard.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/code_assistant/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/code_assistant/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/code_assistant/patch.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/code_assistant/repository.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/code_assistant/service.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/compat/__init__.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/automation.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/capability.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/db.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/demo_mode.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/devices.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/events/__init__.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/events/dispatcher.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/ids.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/jobs.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/notifications.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/protocol.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/provider.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/reasoning.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/security.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/study_session.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/compat/time.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/connectivity/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/cli/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/cli/commands.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/control_plane/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/control_plane/gateway.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/control_plane/linkage.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/control_plane/node_registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/control_plane/pairing_service.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/control_plane/session_registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/control_plane/task_coordinator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/node/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/node/daemon.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/project/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/project/coordinator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/project/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/project/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/envelope.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/error.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/heartbeat.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/identity.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/pairing.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/serialization.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/session.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectivity/protocol/task.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/adapters.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/base.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/runtime.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/connectors/vault.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/container/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/container/docker_config.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/builder.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/compression.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/exceptions.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/explain.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/providers/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/providers/agent.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/providers/base.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/providers/decision.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/providers/device.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/providers/memory.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/providers/project.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/ranking.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/resolver.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/schema.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/security.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/snapshot.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/context/types.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/control_center/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/control_center/snapshot.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/conversation/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/conversation/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/conversation/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/conversation/stream.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/daemon/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/daemon/lifecycle.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/daemon/service.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/daemon/shutdown.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/daemon/supervisor.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/deployment/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/deployment/installer.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/deployment/platform_detect.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/ecosystem/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/ecosystem/installer.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/ecosystem/manifest.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/ecosystem/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/errors.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/benchmark.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/criteria.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/evaluator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/exceptions.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/history.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/quality.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/regression.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/report.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/schema.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/scorer.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/security.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/validators/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/validators/base.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/validators/code_validator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/validators/performance_validator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/validators/schema_validator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/validators/security_validator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/evaluation/validators/test_validator.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| nous_runtime/events/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/events/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/events/stream.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/analyzer.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/collector.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/exceptions.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/explain.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/learning.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/pattern.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/policy_optimizer.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/recommendation.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/schema.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/security.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/similarity.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/experience/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/approval.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/broker.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/constitution.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/contracts.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/delegation.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/enterprise.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/gate.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/lease.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/risk_engine.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/runtime_mode.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/governance/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/inspector/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/inspector/diagnostics.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/inspector/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/inspector/snapshot.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/_compact.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/cache.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/consistency.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/decisions/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/decisions/provider.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/decisions/recovery.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/decisions/retrieval.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/engine.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/evaluator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/explanation.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/history.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/lifecycle.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policies/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policies/base.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policies/composite.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policies/fallback.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policies/override.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policies/rule.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policies/static.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/policy_loader.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/discovery.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/freshness.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/mapping.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/observations.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/probes.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/profiles/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/circuit_breaker.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/classifier.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/executor.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/fallback.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/fault_injection.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/retry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/reliability/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/replay.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/scheduler.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/intelligence/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/classifier.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/explain.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/intent.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/resolver.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/interaction/router.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/kernel/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/kernel/config.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/kernel/object_model.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/kernel/runtime.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/kernel/tracing.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/knowledge/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/knowledge/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/knowledge/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/knowledge/service.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/knowledge/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/learning/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/learning/experience.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/learning/optimizer.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/learning/session.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/learning/state.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/locking.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/marketplace/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/marketplace/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/marketplace/security.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/model/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/model/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/model/runtime.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/model/selector.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/model/types.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/monitoring/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/monitoring/health.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/monitoring/metrics.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/discovery.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/health.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/session.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/network/topology.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/operations/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/operations/node_manager.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/operations/release.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/operations/security_hardening.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/pack/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/pack/loader.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/pack/manifest.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/pack/registry.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/planner/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/dispatcher.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/evaluator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/goal.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/graph.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/observation.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/pipeline.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/plan.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/progress.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/scheduler.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/planner/tool_router.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/platform/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/platform/adapter.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/plugins/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/plugins/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/plugins/manager.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/plugins/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/plugins/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/plugins/runner.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/plugins/security.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/project/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/project/memory.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/project/memory_context.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/project/memory_ingestor.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/project/memory_records.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/project/scan.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/project/workspace.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/provider/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/provider/adapters/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/provider/adapters/audio.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/provider/adapters/chromadb.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/provider/adapters/device_android.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/provider/adapters/device_pc.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/provider/adapters/embed.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/provider/adapters/notification.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/provider/adapters/openai.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/provider/adapters/web.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/provider/base.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/provider/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/provider/router.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/recovery_runtime.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/backends/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/backends/base.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/backends/local.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/backends/persistent_local.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/backends/qdrant.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/embeddings.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/errors.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/evaluation.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/exporter.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/filters.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/gateway.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/hybrid.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/indexing.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/inspector.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/jobs.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/manager.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/protocol.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/ranking.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/records/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/records/hashing.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/records/mapper.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/retrieval/taskgraph.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/lifecycle.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/orchestrator.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/pipeline.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/request.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/response.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/session.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/runtime/trace.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/advanced.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/agent.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/capability.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/client.js | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/client.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/developer.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/harness.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sdk/task.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/security/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/capabilities.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/database.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/events.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/jobs.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/lifecycle.py | INCLUDE | SOURCE | Distributed Runtime source; retained after Ruff and compile validation. Legacy backends remain optional and fail unavailable. |
| nous_runtime/services/packs.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/providers.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/services/traces.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/sqlite_runtime.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/state/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/state/ownership.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/update/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/update/manager.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/version.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workflow/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workflow/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workflow/compiler.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workflow/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workflow/runtime.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workflow/store.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/__init__.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/cli.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/isolation.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/models.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/policy.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/registry.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/resolver.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| nous_runtime/workspace/snapshot.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| packs/examples/hello_pack/pack.yaml | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| packs/examples/study_pack/pack.yaml | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| packs/examples/study_pack/prompts.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| packs/examples/study_pack/subjects.py | INCLUDE | SOURCE | Public SOURCE candidate; retain after final staged review. |
| pyproject.toml | INCLUDE | CONFIGURATION | Public CONFIGURATION candidate; retain after final staged review. |
| README.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| README.zh-CN.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| README_zh.md | EXCLUDE | DUPLICATE | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| remote_terminal/.env.example | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/agent.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain_clients.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain_devices.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain_latex.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain_llm.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain_prompt.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain_sessions.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/brain_utils.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/config.example.json | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/config.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/control_center.html | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/control_center_v2.html | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/course_engine.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/crypto.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/dashboard.html | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/deploy_p0.sh | PRIVATE_ONLY | SCRIPT | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/doc_engine.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/efficiency_engine.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/embedding.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/firewall.ps1 | PRIVATE_ONLY | SCRIPT | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/fix_whitelist.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/formula_engine.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/harden_files.ps1 | PRIVATE_ONLY | SCRIPT | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/health_check.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/learn_db.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/learn_tools.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/learn_upload.html | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/learner_profile.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/memory.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/migrate.sh | PRIVATE_ONLY | SCRIPT | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/nous_core/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/audit/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/automation/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/capability/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/capture.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/config.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/daily_report.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/dashboard.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/db.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/demo_mode.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/devices/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/events/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/events/dispatcher.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/ids.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/jobs/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/learning.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/001_initial.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/002_jobs.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/003_devices.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/004_notifications.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/005_automation.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/006_audit.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/007_inbox.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/008_study_sessions.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/009_capabilities.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/010_capability_graph.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/011_reasoning_trace.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/012_observer.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/013_security.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/migrations/014_stability.sql | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/notifications/__init__.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/notify_bridge.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/observer.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/protocol.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/provider.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/reasoning.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/router.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/security.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/stability.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/study_session.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_core/time.py | INCLUDE | SOURCE | Required compatibility-kernel source; packaged and validated with focused import and Runtime tests. |
| remote_terminal/nous_edge/__init__.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/patch_wake.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/patch_wake2.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/patch_wake3.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/plan_engine.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/requirements.txt | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/reviewer.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/safety.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/schedule_engine.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/seed_caps.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/skill_engine.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/skills/code_engineer.json | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/skills/desktop_operator.json | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/skills/phone_operator.json | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/skills/study_tutor.json | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/skills/watch_operator.json | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/skills/workflow_assistant.json | PRIVATE_ONLY | CONFIGURATION | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/start_agent.bat | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/start_brain.sh | PRIVATE_ONLY | SCRIPT | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/static/upload.html | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/study_manager.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/study_planner.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/subject_experts.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/test_failure_recovery.py | PRIVATE_ONLY | TEST | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/test_p0_events.py | PRIVATE_ONLY | TEST | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/tools.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/vector_store.py | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/watchdog.ps1 | PRIVATE_ONLY | SCRIPT | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| remote_terminal/web_panel.html | PRIVATE_ONLY | SOURCE | Unsupported legacy Remote Terminal application; excluded from package discovery, wheel contents, and public import. |
| RemoteTerminal/app/build.gradle.kts | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/AndroidManifest.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/AppDatabase.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/AudioRecorder.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/ChatScreen.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/ChatWorker.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/CloudTTS.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/Commands.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/Config.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/DevicesScreen.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/DocsScreen.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/I18n.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/KeepAliveService.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/LocalMessage.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/MainActivity.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/MarkdownText.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/MessageDao.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/MindMapCanvas.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/MindMapScreen.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/NetworkMonitor.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/NousAccessibilityService.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/PetCat.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/PhoneControlServer.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/ReminderScheduler.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/SessionsScreen.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/StudyDashboard.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/StudyPlanScreen.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/StudyScreen.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/Theme.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/TimetableGrid.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/TTSHelper.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/TunnelManager.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/VoiceInputHelper.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/java/com/example/remoteterminal/WakeWordService.kt | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable/cat_anim_alert.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable/cat_anim_done.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable/cat_anim_error.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable/cat_anim_idle.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable/cat_anim_sleep.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable/cat_anim_thinking.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable/cat_anim_working.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_alert_1.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_alert_2.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_alert_3.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_done_1.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_done_2.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_done_3.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_error_1.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_error_2.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_error_3.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_idle_1.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_idle_2.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_idle_3.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_sleep_1.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_sleep_2.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_sleep_3.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_thinking_1.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_thinking_2.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_thinking_3.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_working_1.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_working_2.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/drawable-nodpi/cat_working_3.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-hdpi/ic_launcher.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-hdpi/ic_launcher_round.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-mdpi/ic_launcher.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-mdpi/ic_launcher_round.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-xhdpi/ic_launcher.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-xhdpi/ic_launcher_round.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-xxhdpi/ic_launcher.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/values/strings.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/values/themes.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/xml/accessibility_service_config.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/app/src/main/res/xml/network_security_config.xml | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/build.gradle.kts | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/gradle.properties | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/gradle/wrapper/gradle-wrapper.jar | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/gradle/wrapper/gradle-wrapper.properties | EXCLUDE | CONFIGURATION | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/gradlew | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/gradlew.bat | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/local.properties.example | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| RemoteTerminal/settings.gradle.kts | EXCLUDE | SOURCE | Android client is Experimental/Unverified and is outside the v0.1.0-alpha release gate. |
| ROADMAP.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| scripts/benchmark/database_benchmark.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/benchmark/model_runtime_benchmark.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/benchmark/resource_benchmark.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/benchmark/retrieval_benchmark.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/benchmark/run_phase9_baseline.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/benchmark/scheduler_benchmark.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/benchmark/startup_benchmark.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/benchmark/test_suite_profile.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| scripts/benchmark_scheduler.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/healthcheck.sh | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/nous-doctor.sh | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/phase7_builder.py | EXCLUDE | SCRIPT | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| scripts/security_scan.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/smoke_test_clean_install.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/soak/failure_collector.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/soak/resource_monitor.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/soak/runtime_soak_test.py | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/validate_clean_install.ps1 | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| scripts/validate_clean_install.sh | INCLUDE | SCRIPT | Public SCRIPT candidate; retain after final staged review. |
| SECURITY.md | INCLUDE | SECURITY | Public SECURITY candidate; retain after final staged review. |
| SOFTWARE_DESIGN.md | EXCLUDE | ARCHITECTURE | Generated, duplicate, obsolete, cache, build, or runtime artifact. |
| SUPPORT.md | INCLUDE | USER_DOCUMENTATION | Public USER_DOCUMENTATION candidate; retain after final staged review. |
| tests/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/conftest.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_builder.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_models.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_providers.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_resolver.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_runtime_upgrades.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_security.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_snapshot.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/context/test_store.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/evaluation/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/evaluation/test_criteria.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/evaluation/test_eval_security.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/evaluation/test_models.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/evaluation/test_regression.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/evaluation/test_scoring.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/evaluation/test_validators.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/experience/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/experience/test_collector.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/experience/test_models.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/experience/test_pattern.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/experience/test_security.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/experience/test_store.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_api_identity_propagation.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_api_route_enforcement.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_api_security.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_approval_lease_delegation.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_constitution_and_risk.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_constitution_release_gate.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_enterprise_alpha.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_envelope_security.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_gate_lease_consumption.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_gate_release_gate.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_gate_strict_and_concurrency.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_hash_and_scope.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_http_server_security.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_proposal_binding_release_gate.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_provider_gate_release.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_runtime_mode.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/governance/test_scope_release_matrix.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/network/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/network/test_network.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/reference_pareto.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_agent_adapters.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_agent_contract.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_agent_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_approval_broker.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_architecture/test_import_boundaries.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_architecture/test_provider_boundaries.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_architecture/test_route_boundaries.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_architecture/test_runtime_boundaries.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_architecture/test_state_ownership.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_capability/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_capability/test_resolver.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_capability_availability.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_capability_manifest.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_chat_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_cli/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_cli/test_imports.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_cli/test_migrations.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_cli/test_pack_lifecycle.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_cli/test_public_contract.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_code_assistant.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/conftest.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/test_clean_install.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/test_process_boundary.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/test_project_restart.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/test_protocol.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/test_traceability.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connectivity/test_vertical_slice.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_connector_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_conversation_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_decision_lifecycle_store.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_developer_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_events_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_inspector.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_installer.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_kernel/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_kernel/test_tracing.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_knowledge_library.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_learning/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_learning/test_experience.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_learning/test_state.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_local_memory.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_local_retrieval_backend.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_memory_engine.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_multi_agent_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_observation.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_open_source_hygiene.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_p5_7_2_execution_closure.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_pack/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_pack/test_manifest.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_pareto_correctness.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_performance_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_phase7_production.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_phase8_runtime_closure.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_planner/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_planner/test_execution_observation.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_planner/test_goal.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_planner/test_plan.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_plugin_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_product_runtime_integration.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_profiles.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_project_scan.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_project_workspace.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_provider/__init__.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_provider/test_base.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_provider/test_cli_compat.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_provider/test_router.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_provider_reliability_integration.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_rc_security_hardening.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_recovery_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_reliability.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_acl.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_backend_contract.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_fts.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_gateway_generation.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_gateway_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_indexing.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_inspector_cli.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_models.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_pipeline_extensions.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_productionization.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_retrieval_records.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_runtime_dashboard.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_runtime_intelligence.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_scheduler.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_sqlite_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_terminal_product_experience.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_terminal_shell.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_version_consistency.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| tests/test_workflow_runtime.py | INCLUDE | TEST | Public TEST candidate; retain after final staged review. |
| .github/DISCUSSION_GUIDELINES.md | INCLUDE | GOVERNANCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/design/EXECUTION_APPROVAL_EXPERIENCE.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/design/TERMINAL_EXPERIENCE_GUIDE.md | PRIVATE_ONLY | ARCHITECTURE | Internal development material contains local paths or unresolved encoding; do not publish. |
| docs/development/WINDOWS_LOCAL_DEVELOPMENT.md | PRIVATE_ONLY | DEVELOPER_DOCUMENTATION | Internal development material contains local paths or unresolved encoding; do not publish. |
| docs/FAQ.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/getting-started/INSTALLATION.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/getting-started/QUICK_START.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/MIGRATION_GUIDE.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/release/ANNOUNCEMENT_DRAFT.md | INCLUDE | RELEASE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/release/TERMINAL_DEMO_PLAN.md | INCLUDE | RELEASE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/release/WEBSITE_LAUNCH_PLAN.md | INCLUDE | RELEASE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/rfcs/0000-template.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/specs/CONNECTOR_SPEC.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/specs/NODE_SPEC.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/specs/PLUGIN_SPEC.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/specs/PROVIDER_SPEC.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/specs/RUNTIME_SPEC.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| docs/specs/WORKFLOW_SPEC.md | INCLUDE | ARCHITECTURE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_connector/connector.json | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_connector/README.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_connector/run_example.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_plugin/capabilities.json | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_plugin/plugin.json | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_plugin/plugin_impl.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_plugin/README.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_provider/hello_provider.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_runtime/README.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/hello_workflow/README.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/README.md | INCLUDE | DEVELOPER_DOCUMENTATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/sdk/python_quickstart.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| examples/sdk/typescript_quickstart.ts | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| ide/vscode/package.json | INCLUDE | CONFIGURATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| ide/vscode/README.md | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| ide/vscode/src/extension.ts | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| ide/vscode/tsconfig.json | INCLUDE | CONFIGURATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| NOTICE | INCLUDE | LEGAL | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/__main__.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/cli/execution_ui.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/cli/provider_experience.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/ide/__init__.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/ide/protocol.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/provider/adapters/anthropic.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/provider/credentials.py | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/sdk/client.ts | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/sdk/package.json | INCLUDE | CONFIGURATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/sdk/README.md | INCLUDE | SOURCE | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| nous_runtime/sdk/tsconfig.json | INCLUDE | CONFIGURATION | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| tests/test_cli_entry.py | INCLUDE | TEST | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| tests/test_extension_examples.py | INCLUDE | TEST | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| tests/test_provider/test_experience.py | INCLUDE | TEST | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| tests/test_runtime_ecosystem.py | INCLUDE | TEST | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
| tests/test_terminal_execution_approval.py | INCLUDE | TEST | Validated Sprint 13-19 or final productization candidate; include in the Alpha public tree. |
## Totals

| Decision | Count |
| --- | ---: |
| INCLUDE | 735 |
| EXCLUDE | 229 |
| PRIVATE_ONLY | 263 |
| REWRITE | 0 |
| LEGAL_REVIEW | 0 |
| Total | 1227 |

## Release boundary

Only INCLUDE rows are eligible for a later maintainer-approved clean public copy. EXCLUDE and PRIVATE_ONLY rows must not be copied. The manifest does not authorize copying, staging, committing, tagging, pushing, or publication.
