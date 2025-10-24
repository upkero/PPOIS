from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VIPLounge:
    lounge_name: str
    airport: Airport
    capacity: int
    guests: list[Passenger] = field(default_factory=list)

    def admit_guest(self, passenger: Passenger) -> bool:
        if len(self.guests) >= self.capacity:
            return False
        self.guests.append(passenger)
        return True

    def current_load(self) -> int:
        return len(self.guests)
