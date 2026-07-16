# PLUGIN SPEC

Plugins declare version, checksum, capabilities, permissions, and isolation requirements. Undeclared capability, permission, network, or filesystem access is denied; failures remain isolated.

## Compatibility

Versioned contracts must remain backward compatible during Alpha unless a security boundary requires fail-closed rejection.
