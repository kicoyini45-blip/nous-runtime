# Nous Runtime

Nous is a long-lived intelligent runtime built to serve people, helping them understand, create, and operate complex systems.

Nous is local-first. It coordinates conversation, agents, workflows, knowledge, tools, approvals, events, recovery, and connected nodes through a governed Runtime. The Server Runtime remains authoritative; terminal and device clients are control surfaces.

Current target: `v0.1.0-alpha`.

## Why Nous

Complex work often outlives one prompt, one process, or one device. Nous keeps durable context and execution evidence while making state transitions, approvals, failures, and recovery visible to the user. It is designed around explicit ownership boundaries and user-controlled actions.

## Core Capabilities

- Persistent conversations with bounded context, rolling summaries, paginated history, and streaming export.
- Agent and multi-agent execution through shared Runtime, workspace, governance, event, and artifact contracts.
- Governed workflows, plugins, connectors, and knowledge retrieval.
- Capability-aware scheduling, resource limits, recovery, replay, and inspection.
- Terminal-native operation with JSON and non-interactive modes.
- Server-authoritative control for local and connected devices.

## Architecture

```text
Terminal / SDK / HTTP / Mobile / Node
                 |
          Server Runtime
                 |
 Intent -> Context -> Decision -> Governance -> Execution
                 |                       |
          ConversationStore       ApprovalBroker
                 |
     RunStore / EventStream / Workflow / Agent
                 |
  Capability / Plugin / Connector / Knowledge / Node
```

Authoritative state stays in the established Runtime stores and registries. Clients do not create parallel Run, Event, Conversation, Approval, Workflow, Capability, Node, or Workspace state.

## Quick Start

Python 3.10 or newer is required.

```bash
git clone https://github.com/kicoyini45-blip/nous-runtime.git
cd nous-runtime
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -e .
nous
```

On Linux:

```bash
. .venv/bin/activate
python -m pip install -e .
nous
```

The first interactive launch can create a local `.nous` workspace. Provider configuration is optional for local inspection commands but required for model-backed conversation.

## Terminal Experience

Running `nous` opens the persistent terminal interface. Natural-language input follows the governed execution path. Core commands include:

```text
/status    /runs      /run show   /approve
/pause     /resume    /cancel     /dashboard
/inspect   /context   /files      /tests
/clear     /help      /quit
```

Additional terminal behavior:

- `Ctrl+C` cancels the active operation and keeps the session open.
- `Ctrl+D` or `/quit` closes the client cleanly.
- `--session ID` reconnects to a conversation.
- `--json` emits JSON Lines; `--quiet` suppresses terminal chrome.
- `--no-color` and the `NO_COLOR` environment variable disable styled output.
- Piped input uses a non-TTY fallback without prompts.
- Conversation history and event replay are loaded in bounded pages.

## Security Model

Nous applies authorization, policy, and approval before governed actions. Plugins and connectors are expected to fail closed when declarations, permissions, versions, checksums, or isolation requirements are not satisfied. Workspace and library identifiers are propagated through Runtime requests.

The alpha does not claim to be an operating-system sandbox. Process, container, and device isolation depend on the configured platform. The default HTTP binding is localhost; operators must add authentication and transport controls before exposing it beyond a trusted host.

Never commit credentials, private keys, databases, conversation logs, runtime JSONL state, or local configuration.

## Alpha Scope

`v0.1.0-alpha` is intended for local development, integration evaluation, and review of the Runtime contracts. It includes the terminal client, HTTP Runtime surfaces, governed product integrations, recovery, inspection, SDK primitives, and experimental multi-device support.

Alpha interfaces may change before a stable release. Compatibility is maintained where documented, but no production availability or security certification is implied.

## Known Limitations

- Model-backed conversation requires a configured compatible provider.
- Some optional retrieval, speech, document, and UI features require extra dependencies.
- Plugin isolation is limited to configured isolation backends; untrusted in-process execution is not treated as isolated.
- Multi-node and mobile paths are alpha and require explicit pairing and deployment configuration.
- Workflow cancellation for trusted in-process handlers is cooperative.
- Windows and Linux receive the primary terminal coverage; other platforms are not yet release targets.

## Platform Support

| Surface | Alpha support |
| --- | --- |
| Windows Terminal and PowerShell | Supported |
| Linux terminals | Supported |
| Chinese and Unicode | Supported |
| Non-TTY / JSON Lines | Supported |
| HTTP Server Runtime | Supported for local use |
| Android control client | Experimental |
| Distributed nodes | Experimental |

## Development

```bash
python -m pip install -e ".[dev]"
python -m ruff check nous_runtime tests
python -m compileall nous_runtime
python -m pytest -q
```

Tests may create local Runtime state. Use a disposable workspace and do not add generated state to source control.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md) before proposing a change. Contributions should preserve authoritative state ownership, fail-closed security behavior, bounded resource use, and user control.

## License

Apache License 2.0. See [LICENSE](LICENSE). Third-party notices and dependency licenses remain subject to their respective terms.
