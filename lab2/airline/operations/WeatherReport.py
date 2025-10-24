from __future__ import annotations

from dataclasses import dataclass


@dataclass
class WeatherReport:
    airport: Airport
    condition: str
    temperature_c: float
    wind_speed: float

    def is_safe_for_takeoff(self) -> bool:
        return self.condition.lower() not in {"storm", "hail"} and self.wind_speed < 25

    def update_condition(self, condition: str, wind_speed: float) -> None:
        self.condition = condition
        self.wind_speed = wind_speed
