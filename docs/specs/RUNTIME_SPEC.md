# RUNTIME SPEC

Runtime is the authoritative long-lived execution service. Clients submit intent and read canonical Run, Event, Approval, Conversation, Workspace, and Recovery state; they do not own it.

## Compatibility

Versioned contracts must remain backward compatible during Alpha unless a security boundary requires fail-closed rejection.
