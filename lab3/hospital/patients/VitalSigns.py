from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VitalSigns:
    heart_rate: int
    blood_pressure: str
    temperature_c: float
    oxygen_saturation: int

    def is_stable(self) -> bool:
        return 36 <= self.temperature_c <= 37.5 and 95 <= self.oxygen_saturation <= 100

    def update_temperature(self, new_temp: float) -> None:
        self.temperature_c = new_temp
