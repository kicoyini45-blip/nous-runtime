"""Model Runtime facade."""

from __future__ import annotations

from nous_runtime.model.selector import ModelSelector
from nous_runtime.model.types import ModelRequest, ModelSelection


class ModelRuntime:
    def __init__(self, selector: ModelSelector | None = None):
        self.selector = selector or ModelSelector()

    def select(self, request: ModelRequest) -> ModelSelection:
        return self.selector.select(request)
