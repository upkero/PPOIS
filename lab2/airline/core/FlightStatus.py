from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class FlightStatus:
    code: str
    description: str
    last_updated: datetime

    def mark_delayed(self, reason: str) -> None:
        self.code = "DELAYED"
        self.description = reason
        self.last_updated = datetime.now()

    def is_operational(self) -> bool:
        return self.code not in {"CANCELLED", "DELAYED"}
