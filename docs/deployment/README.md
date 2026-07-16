# Deployment

The alpha release is intended for local development and controlled environments.

Deployment requirements:

- Use strong authentication tokens.
- Keep secrets in local environment variables or private config files.
- Keep runtime state, logs, and databases out of Git.
- Place network-facing services behind an authenticated gateway, firewall, or private encrypted network.
- Run `nous doctor`, `nous demo`, and the test suite before publishing an environment.
