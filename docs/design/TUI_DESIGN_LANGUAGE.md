# Nous Terminal UI Design Language

## Purpose

Nous is a terminal-native conversation and control surface for a long-lived Runtime. It should feel like entering a durable engineering system: calm, precise, keyboard-first, and visually restrained.

The Server Runtime remains authoritative. The terminal owns only local editing, completion selection, folding, viewport, and color state.

## Identity

Wide and standard terminals use the monochrome NOUS ASCII wordmark. Compact terminals use `N O U S`. The logo appears once at session entry and must not dominate the working surface.

The Header exposes Workspace, Session, Provider, Model, Path, Runtime, and Version. It does not contain slogans, capability inventories, memory counters, private configuration, credentials, or diagnostic traces.

## Information boundaries

Three content streams must remain visually and semantically separate:

- **Conversation:** user input and Nous responses.
- **Runtime:** transient operational activity, completion, warning, failure, and cancellation.
- **Message:** the persistent input viewport.

Runtime events are not assistant messages. Input text is not a Runtime event. Presentation labels are not canonical Runtime states.

## Layout

At 140 columns and above, Message and Runtime form a restrained two-column footer. At 80–139 columns they stack beneath Conversation. Below 80 columns the compact identity and single-column surface are used.

The Message region always has an explicit boundary. The status bar remains visible below it. Incremental redraw is limited to completion, Runtime, Message, and status regions.

## Interaction

Slash completion uses strict prefix matching, at most eight visible candidates, contextual arguments, and authoritative identifiers. Tab accepts, arrows navigate, Escape dismisses, Enter submits, and F1 opens help.

Ctrl+C cancels active work without closing the session. Cancellation appears once in Runtime and does not pollute Conversation. Ctrl+D exits only from empty input.

## Dashboard and Inspector

Dashboard uses compact cards for Runtime, Scheduler, Memory, Events, Providers, Workspace, Performance, and Queue. Inspector uses a collapsed read-only tree and expands one requested branch at a time.

Both surfaces render existing snapshots only. They do not introduce navigation state, persistence, or alternative ownership.

## Color and motion

Prefer spacing, alignment, and typography over borders. Rounded input and compact card boundaries may be used where they clarify ownership.

Use a monochrome base with muted informational cyan, completion green, warning yellow, and failure red. Respect `NO_COLOR`. Do not use emoji, gradients, blinking, aggressive animation, or repeated spinner repaint. Activity changes only when meaningful work stages change.
