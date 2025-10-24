from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Procedure:
    code: str
    name: str
    duration_minutes: int
    requires_anesthesia: bool

    def estimate_cost(self, rate_per_minute: float) -> float:
        return self.duration_minutes * rate_per_minute

    def is_major(self) -> bool:
        return self.duration_minutes > 120 or self.requires_anesthesia
