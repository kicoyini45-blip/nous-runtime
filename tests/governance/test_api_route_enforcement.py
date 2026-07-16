from types import SimpleNamespace

from nous_runtime.api import routes


def test_parameterized_route_matches_valid_segment(monkeypatch):
    monkeypatch.setenv("NOUS_API_TOKEN", "secret")
    monkeypatch.setitem(
        routes.ROUTES,
        ("DELETE", "/api/v1/packs/{name}"),
        lambda name: routes.ok_response({"removed": name}),
    )
    monkeypatch.setattr(routes, "_authorize_mutation_route", lambda *args, **kwargs: None)

    response = routes.route(
        "DELETE",
        "/api/v1/packs/example-pack",
        auth={"token": "secret"},
    )

    assert response == {"ok": True, "data": {"removed": "example-pack"}}


def test_parameterized_route_rejects_encoded_traversal(monkeypatch):
    monkeypatch.setenv("NOUS_API_TOKEN", "secret")

    response = routes.route(
        "DELETE",
        "/api/v1/packs/%2e%2e",
        auth={"token": "secret"},
    )

    assert response["ok"] is False
    assert response["error"]["code"] == "NOUS_INVALID_REQUEST"


def test_path_parameter_cannot_be_overridden(monkeypatch):
    monkeypatch.setenv("NOUS_API_TOKEN", "secret")
    monkeypatch.setattr(routes, "_authorize_mutation_route", lambda *args, **kwargs: None)

    response = routes.route(
        "DELETE",
        "/api/v1/packs/example-pack",
        params={"name": "other-pack"},
        auth={"token": "secret"},
    )

    assert response["ok"] is False
    assert response["error"]["code"] == "NOUS_INVALID_REQUEST"


def test_server_pack_mutation_is_governed_before_handler(monkeypatch):
    captured = {}

    class Gate:
        def evaluate(self, proposal, context):
            captured["proposal"] = proposal
            captured["context"] = context
            return SimpleNamespace(
                action_mode="ASK_APPROVAL",
                rule_class="USER_APPROVABLE",
                reason_code="APPROVAL_REQUIRED",
                reason_message="Approval required",
                decision_id="decision-a",
            )

    def unexpected_handler(body):
        raise AssertionError("handler must not run before approval")

    monkeypatch.setenv("NOUS_API_TOKEN", "secret")
    monkeypatch.setenv("NOUS_API_SUBJECT", "service-account-a")
    monkeypatch.setattr("nous_runtime.governance.get_gate", lambda: Gate())
    monkeypatch.setitem(routes.ROUTES, ("POST", "/api/v1/packs/install"), unexpected_handler)

    response = routes.route_server(
        "POST",
        "/api/v1/packs/install",
        body={"path": "./pack"},
        auth={"token": "secret"},
    )

    assert response["ok"] is False
    assert response["error"]["code"] == "NOUS_APPROVAL_REQUIRED"
    assert captured["proposal"].capability_id == "pack.install"
    assert captured["context"].subject_id == "service-account-a"
