from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Seat:
    seat_number: str
    cabin_class: str
    is_available: bool = True
    passenger: Passenger | None = None

    def assign_passenger(self, passenger: Passenger) -> None:
        self.passenger = passenger
        self.is_available = False

    def release(self) -> None:
        self.passenger = None
        self.is_available = True
