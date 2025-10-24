from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Schedule:
    departure_time: datetime
    arrival_time: datetime
    gate: Gate | None = None
    terminal: Terminal | None = None
    status: str = "scheduled"

    def update_times(self, new_departure: datetime, new_arrival: datetime) -> None:
        self.departure_time = new_departure
        self.arrival_time = new_arrival

    def assign_gate(self, gate: Gate, terminal: Terminal) -> None:
        self.gate = gate
        self.terminal = terminal
        gate.reserve_for_schedule(self)
