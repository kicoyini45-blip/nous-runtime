# Contributing to Nous Runtime

Nous Runtime accepts focused changes with tests and clear ownership boundaries. Open an issue before broad design work. Keep Run, Event, Approval, Conversation, Workflow, Connector, Node, and Workspace ownership authoritative; do not create parallel Stores or state machines.

## Development

Create an isolated environment, install development dependencies, run Ruff and the tests affected by your change, and document user-visible behavior. Never commit credentials, local Runtime state, databases, conversation logs, or private paths.

Pull requests should explain the problem, scope, tests, compatibility impact, security impact, and documentation changes. Maintainers review and merge changes; contributors must not bypass governance or approval controls.
