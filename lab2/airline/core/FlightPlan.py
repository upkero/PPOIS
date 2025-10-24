from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FlightPlan:
    route: Route
    cruising_altitude_ft: int
    fuel_required_kg: float
    weather_notes: list[str] = field(default_factory=list)

    def adjust_fuel(self, extra_percentage: float) -> None:
        if extra_percentage < 0:
            raise ValueError("Extra percentage cannot be negative.")
        self.fuel_required_kg *= 1 + extra_percentage / 100

    def add_weather_note(self, note: str) -> None:
        self.weather_notes.append(note)
