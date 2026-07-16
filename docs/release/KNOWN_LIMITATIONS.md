# Known Limitations

Version: `v0.1.0-alpha`

- Model-backed conversation requires a configured compatible provider.
- Trusted in-process Workflow handlers use cooperative cancellation. Potentially blocking or untrusted handlers require process isolation.
- Plugin isolation depends on an available isolation backend. Untrusted in-process execution is not considered isolated.
- Only remote_terminal.nous_core is distributed as a compatibility kernel. The unsupported top-level Remote Terminal application is excluded from package discovery and public import.
- Desktop and VS Code are Alpha MVP control surfaces. Run-event updates use bounded HTTP replay with sequence cursors rather than a WebSocket push channel.
- Optional retrieval, document, speech, and rich-terminal behavior require extra dependencies.
- Android is Experimental/Unverified, excluded from the v0.1.0-alpha public source set, and not release-gating. Distributed-node paths remain experimental and require explicit pairing, authentication, and deployment configuration.
- The HTTP Server defaults to localhost. TLS and externally exposed deployment controls are operator responsibilities.
- Nous does not provide a general operating-system sandbox.
- Alpha APIs and persisted formats may change before a stable release.
- Windows and Linux are the primary terminal targets; other platforms are not validated release targets.
