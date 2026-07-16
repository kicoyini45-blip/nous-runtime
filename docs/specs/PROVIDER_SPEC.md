# Provider Spec

Providers declare capabilities, endpoint protocol, model, context window, locality, health, and credential references. Secrets are resolved at invocation and never persisted in Provider configuration.

## Service and protocol

The terminal configuration layer presents services that users recognize. Each service maps to an existing Provider protocol and Registry entry; the service layer does not introduce a second Provider state machine.

| Service | Existing Provider type |
|---|---|
| OpenAI, DeepSeek, OpenRouter, SiliconFlow, Moonshot AI, Azure OpenAI | OpenAI compatible |
| Claude | Anthropic compatible |
| Ollama | Ollama |
| Generic OpenAI Compatible, Local HTTP, Custom Provider | Existing advanced types |

Service presets supply editable endpoint and credential-reference defaults. The stored invocation endpoint remains explicit so existing Provider adapters continue to own request execution. The Azure OpenAI preset uses `AZURE_OPENAI_AUTH_TOKEN` because the existing OpenAI-compatible adapter sends Bearer credentials; it does not mislabel an Azure API key as a Bearer token.

## Credentials

Provider configuration may contain only a credential reference and safe metadata. Supported interaction choices are environment references, operating-system secret storage, process-scoped one-time input, or no credential. Process-scoped credentials are unavailable after restart by design. Dashboard, test, ping, and Doctor output must never reveal resolved secret values.

## Model discovery and diagnostics

The Wizard may issue a bounded, read-only model-catalog request. Failure to list models does not mutate Provider state; the user may select a documented fallback or enter a model explicitly. `/provider doctor` performs bounded diagnostics for endpoint reachability, credential availability, authentication, selected-model discovery, protocol streaming support, and latency. Protocol support must not be reported as an exercised streaming test.

## Capability ownership

Service presets map only to existing capability identifiers. Provider Registry, Capability Registry, Governance, Approval, and Runtime scheduling retain their existing authority. The configuration experience does not create capabilities or bypass capability availability checks.

## Compatibility

Versioned contracts must remain backward compatible during Alpha unless a security boundary requires fail-closed rejection. Protocol-oriented preset entry points remain compatibility adapters for existing callers.
