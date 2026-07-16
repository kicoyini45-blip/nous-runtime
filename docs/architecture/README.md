# Architecture

Nous Runtime is organized around authoritative state owners and a shared governed execution path.

| State or lifecycle | Authority |
| --- | --- |
| Runs | RunStore |
| Events | EventStream / EventStore |
| Approvals | ApprovalBroker and approval persistence |
| Conversations | ConversationStore |
| Workflow definitions | Workflow Registry / Workflow Store |
| Workflow execution | TaskGraph, Run, and Event systems |
| Plugin lifecycle and capabilities | Plugin Registry and Capability Registry |
| Connectors | Connector Registry / Connector Store |
| Knowledge | Knowledge / Library Store and Retrieval Gateway |
| Agents | Agent Runtime |
| Nodes and workspaces | Node Registry and Workspace Store |

Terminal, SDK, HTTP, desktop, mobile, and node clients are views and control surfaces. The Server Runtime remains authoritative.

The shared product path is:

```text
Input -> Intent -> Context -> Decision -> Governance -> Execution
      -> Event / Artifact -> Evaluation -> Recovery or Result
```

Historical audit material is private release evidence and is not part of the public architecture documentation.
