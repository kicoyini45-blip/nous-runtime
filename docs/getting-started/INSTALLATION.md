# Installation

Nous Runtime requires Python 3.10 or newer.

## Minimal install

```console
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install nous-runtime==0.1.0a0
nous version
```

On Linux, activate with `source .venv/bin/activate`.

## Terminal UI

```console
python -m pip install "nous-runtime[ui]==0.1.0a0"
nous
```

The HTTP Server binds to localhost by default. Configure `NOUS_API_TOKEN` before using Server, Desktop, IDE, or SDK control paths. Do not expose the Alpha Server directly to an untrusted network; TLS and external access controls are operator responsibilities.

Optional retrieval, document and speech dependencies are intentionally not installed by the minimal or UI profiles.
