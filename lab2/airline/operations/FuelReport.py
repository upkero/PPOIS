from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FuelReport:
    flight: Flight
    fuel_loaded_kg: float
    fuel_required_kg: float
    variance: float = 0.0

    def compute_variance(self) -> float:
        self.variance = self.fuel_loaded_kg - self.fuel_required_kg
        return self.variance

    def needs_top_up(self, tolerance: float = -500.0) -> bool:
        return self.compute_variance() < tolerance
