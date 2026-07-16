# Alpha Scope

Version: `v0.1.0-alpha`

## Included

The alpha contains the Server Runtime pipeline; persistent terminal conversations; Scheduler and resource controls; EventStream and recovery; Context and Retrieval runtimes; Chat, Code Assistant, Multi-Agent, Workflow, Knowledge, Plugin, and Connector integrations; governance and approvals; SDK and inspection tools; HTTP control surfaces; and experimental node control paths.

These capabilities share the established Runtime state owners and governance path. Their inclusion does not imply stable APIs, production availability, or an operating-system sandbox.

## Release boundary

The alpha is intended for local development, integration evaluation, and contract review. Security-sensitive deployments require independent configuration and review. Optional model, retrieval, document, speech, mobile, and isolation features require their documented dependencies or platform services.

No production support, uptime commitment, compatibility guarantee, or security certification is provided.

## Experimental exclusions

The legacy Android client is Experimental/Unverified for v0.1.0-alpha. It is not part of the public source set, its Gradle build is not an Alpha release gate, and no Android support claim is made. A later release may requalify a clean mobile client against a documented JDK and Android toolchain.
