from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BaggageTag:
    tag_id: str
    passenger: Passenger
    flight: Flight
    luggage_weight: float

    def update_weight(self, new_weight: float) -> None:
        self.luggage_weight = new_weight

    def format_label(self) -> str:
        return f"{self.tag_id}:{self.passenger.name}:{self.flight.number}"
