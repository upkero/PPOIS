from __future__ import annotations

from dataclasses import dataclass, field

from airline.exceptions.SecurityAlertException import SecurityAlertException
from airline.exceptions.UnauthorizedAccessException import UnauthorizedAccessException


@dataclass
class SecurityCheck:
    checkpoint_id: str
    airport: Airport
    waiting_passengers: list[Passenger] = field(default_factory=list)
    confiscated_items: list[str] = field(default_factory=list)

    def add_to_queue(self, passenger: Passenger) -> None:
        if passenger in self.waiting_passengers:
            raise UnauthorizedAccessException("Passenger already in checkpoint queue.")
        self.waiting_passengers.append(passenger)

    def confiscate_item(self, item: str) -> None:
        self.confiscated_items.append(item)
        if item.lower() in {"weapon", "explosive"}:
            raise SecurityAlertException(f"Dangerous item detected: {item}")
