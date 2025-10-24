from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Runway:
    runway_id: str
    length_meters: int
    surface_type: str
    assigned_flight: Flight | None = None

    def assign_flight(self, flight: Flight) -> None:
        self.assigned_flight = flight

    def mark_closed(self) -> None:
        self.assigned_flight = None
