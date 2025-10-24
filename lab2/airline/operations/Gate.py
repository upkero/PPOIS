from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Gate:
    gate_number: str
    terminal: Terminal
    current_flight: Flight | None = None
    status: str = "available"

    def assign_flight(self, flight: Flight) -> None:
        self.current_flight = flight
        self.status = "boarding"

    def reserve_for_schedule(self, schedule: Schedule) -> None:
        self.status = f"reserved for {schedule.departure_time.isoformat()}"
