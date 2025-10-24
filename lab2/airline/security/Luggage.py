from __future__ import annotations

from dataclasses import dataclass, field

from airline.exceptions.LuggageOverweightException import LuggageOverweightException


@dataclass
class Luggage:
    weight: float
    owner: Passenger
    contents: list[str] = field(default_factory=list)
    status: str = "unchecked"

    def add_content(self, item: str) -> None:
        self.contents.append(item)

    def ensure_weight_limit(self, limit: float) -> None:
        if self.weight > limit:
            raise LuggageOverweightException(f"Luggage exceeds weight limit by {self.weight - limit:.1f} kg.")
