# -*- coding: utf-8 -*-
"""
Capability Availability -determine which capabilities are actually usable.

Cross-references the capability database with the live provider registry
to determine which capabilities are available (provider is registered and
healthy) and which are unavailable (provider missing, down, or capability
disabled).

Usage:
    from nous_runtime.capability.availability import check_availability

    result = check_availability()
    print(result["available"])
    print(result["unavailable"])
"""

from __future__ import annotations

from typing import Any


def check_availability() -> dict[str, list[dict[str, Any]]]:
    """
    Return capabilities split into available and unavailable.

    Returns::

        {
            "available": [
                {"name": "model.reason", "provider": "openai", "risk": "low", ...},
                ...
            ],
            "unavailable": [
                {"name": "image.analyze", "reason": "requires vision provider", ...},
                ...
            ],
        }

    A capability is **available** when:
      1. It is enabled in the database
      2. Its declared provider is registered
      3. The registered provider reports health != "down"

    A capability is **unavailable** with a reason string when any check fails.
    """
    available: list[dict[str, Any]] = []
    unavailable: list[dict[str, Any]] = []

    # 1. Get all capabilities from DB
    try:
        from nous_runtime.compat.capability import list_capabilities
        caps = list_capabilities()
    except Exception:
        caps = []

    if not caps:
        return {"available": [], "unavailable": []}

    # 2. Get registered providers and their health
    provider_health: dict[str, str] = {}
    provider_caps: dict[str, set[str]] = {}

    try:
        from nous_runtime.provider.registry import registry
        provs = registry.list_all()
        for p in provs:
            pid = p.get("id", p.get("name", ""))
            health = p.get("health", {}).get("status", "unknown")
            provider_health[pid] = health
            provider_caps[pid] = set(p.get("capabilities", []))
    except Exception:
        pass

    # 3. Classify each capability
    for cap in caps:
        if not isinstance(cap, dict):
            continue

        name = cap.get("name", "?")
        provider = cap.get("provider", "")
        enabled = cap.get("enabled", True)

        # Check: enabled?
        if not enabled:
            unavailable.append({
                "name": name,
                "provider": provider,
                "reason": "capability is disabled",
            })
            continue

        # Check: provider registered?
        if not provider or provider not in provider_health:
            unavailable.append({
                "name": name,
                "provider": provider or "(none)",
                "reason": f"requires {provider or 'a'} provider",
            })
            continue

        # Check: provider healthy?
        health = provider_health[provider]
        if health == "down":
            unavailable.append({
                "name": name,
                "provider": provider,
                "reason": f"provider {provider} is down",
            })
            continue

        # Check: provider declares this capability?
        # (Skip for built-in/demo providers that use wildcards)
        if provider in provider_caps and provider_caps[provider]:
            if name not in provider_caps[provider]:
                # Check wildcard match
                matched = any(
                    name == pc or name.startswith(pc.rstrip("*"))
                    for pc in provider_caps[provider]
                )
                if not matched:
                    unavailable.append({
                        "name": name,
                        "provider": provider,
                        "reason": f"not declared by provider {provider}",
                    })
                    continue

        available.append({
            "name": name,
            "provider": provider,
            "category": cap.get("category", ""),
            "risk": cap.get("risk", "low"),
            "description": cap.get("description", ""),
        })

    # Sort: available first by category, unavailable by name
    available.sort(key=lambda c: (c.get("category", ""), c["name"]))
    unavailable.sort(key=lambda c: c["name"])

    return {"available": available, "unavailable": unavailable}
