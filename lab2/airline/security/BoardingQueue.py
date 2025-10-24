from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class BoardingQueue:
    flight: Flight
    passengers: list[Passenger] = field(default_factory=list)
    priority_rules: list[str] = field(default_factory=list)

    def enqueue_passenger(self, passenger: Passenger) -> None:
        self.passengers.append(passenger)

    def next_passenger(self) -> Passenger | None:
        if not self.passengers:
            return None
        return self.passengers.pop(0)
