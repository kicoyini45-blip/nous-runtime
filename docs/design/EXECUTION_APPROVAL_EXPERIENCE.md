# Execution, Approval, and Control Experience

## Purpose

The terminal presents the lifecycle of governed work without owning it. RunStore-derived Run records, EventStream/EventStore events, ApprovalBroker requests, Governance decisions, Workspace identity, and Recovery assessments remain authoritative. The terminal adds rendering, selection, folding, focus, and command dispatch only.

No percentage, intermediate state, approval, retry, or recovery outcome may be invented for presentation.

## Execution lifecycle

Canonical Run states are presented with restrained user-facing labels:

| Canonical state | Terminal label |
| --- | --- |
| `CREATED` | Received |
| `PLANNING` | Planning |
| `WAITING_FOR_NODE` | Ready |
| `WAITING_FOR_APPROVAL` | Waiting for approval |
| `RUNNING` and `EVALUATING` | Running |
| `PAUSED` | Paused |
| `RECOVERING` | Recovering |
| `COMPLETED` | Succeeded |
| `FAILED` | Failed |
| `CANCELLED` | Cancelled |

Retrying and Denied appear only when persisted events provide that evidence. Completed timeline stages collapse into a count. Active, failed, denied, cancelled, or recovery states remain visible. The UI does not estimate progress.

`/run show RUN_ID [page]` renders the focused timeline, plan evidence, action cards, and failure/recovery evidence from the selected event page. `/run focus RUN_ID` changes terminal focus only. `/runs` and `/tasks` both present the canonical Run and Approval queue; the former `tasks.json` view is not a second task lifecycle.

## Tool action cards

Recognized Event types are grouped into presentation cards for shell commands, file reads and writes, tests, network requests, Plugin and Connector calls, Workflow steps, and Agent delegation.

A card may show:

- action and target;
- Workspace and purpose;
- risk and approval state when recorded;
- duration and result when recorded;
- folded operation or result detail.

Command output remains folded by default and reports the number of hidden events. Cards are bounded and wrap long values. Common credential assignments are redacted before display. Rendering does not change Event payloads or claim missing evidence.

## Approval panel

Pending requests are read from ApprovalBroker. Proposal details are read from the Broker's GovernanceStore using the request's proposal hash. The panel shows action, target, Workspace, required permissions, risk, reason, actor, scope, expiry, side effects, and reversibility when those fields exist.

Interactive decisions are:

1. Allow once
2. Allow for session
3. Edit action
4. Deny

`Y`/`1`, `A`/`2`, `E`/`3`, and `N`/`4` select directly. Arrow keys or Tab move selection, Enter confirms, Escape closes, and Ctrl+O toggles details. The Message input remains visible below the panel.

Allow and Deny always call ApprovalBroker. Self-approval prevention remains enabled. The terminal does not write an approval response directly and does not create approval state.

`Allow once` uses the Broker's one-use, proposal-hash-bound scope. `Allow for session` delegates `scope="session"` to the existing Broker; its effective boundary is still the exact proposal hash and Broker expiry. It is not a capability-wide grant. The current Broker lease is not shortened merely because the terminal process closes, so the terminal must not describe it as process-local authority.

## Approval modes

The terminal offers presets over existing ApprovalPolicy fields:

| Mode | Existing policy mapping | Human gate |
| --- | --- | --- |
| Strict | `always_ask` | Every governed action |
| Balanced | `policy_controlled`, maximum auto risk `low` | Medium, High, Critical |
| Assisted | `policy_controlled`, maximum auto risk `medium` | High, Critical |

Read-only and test overrides remain disabled in these presets so a High-risk label cannot be bypassed by action category. Critical risk is always asked by ApprovalPolicy. Reset restores Strict. Policy changes use ApprovalBroker persistence; the terminal stores only the current display label.

## Editing and plan confirmation

Approval editing is restricted to authorization-bound scope fields: Workspace, affected resources, permissions, data classification, side-effect class, reversibility, retry behavior, and external recipients.

An edit creates a new immutable ActionProposal and sends it through the existing ExecutionAuthorizationGate. It does not approve, execute, supersede, or mutate the original proposal. The original request remains pending, and its Runtime owner must resubmit the edited proposal through the normal governed path. Unsupported or unavailable fields fail closed.

Plan confirmation shows expected files, action summary, declared validation, risk, and rollback evidence. Missing evidence is labelled as not declared rather than inferred.

## Failure and recovery

Failure views show the recorded cause, persisted state, Recovery strategy, and inspection/cancellation commands. Run and Event state are preserved. The current Recovery API does not expose a general manual Retry or Fallback command, so the terminal reports that limitation instead of manufacturing one. Fallback remains controlled by existing reliability policy.

## Responsive behavior

Cards wrap in a single column at compact widths. The fixed footer shows keyboard help, Provider readiness, focused Run, and approval mode. Wide layouts keep Message and Runtime adjacent; narrower layouts stack them. Details remain available on demand rather than occupying the Conversation stream.

## Security invariants

- no self-approval;
- no direct approval persistence from the terminal;
- no widening of proposal-hash scope;
- no execution from an edited preview;
- no inferred risk, identity, permission, or recovery result;
- no credential display from common assignment forms;
- no parallel Run, Event, Approval, task, or recovery state.
