from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Allergy:
    allergen: str
    reaction: str
    severity: str

    def describe(self) -> str:
        return f"{self.allergen} ({self.severity})"

    def requires_alert(self) -> bool:
        return self.severity.lower() in {"severe", "critical"}
