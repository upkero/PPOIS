from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Beverage:
    beverage_name: str
    is_alcoholic: bool
    volume_ml: int

    def chill(self, degrees: float) -> str:
        return f"{self.beverage_name} chilled by {degrees}°C"

    def serving_note(self) -> str:
        return "Serve cold" if not self.is_alcoholic else "Verify age before serving"
