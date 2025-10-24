from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CrewMember:
    name: str
    role: str
    certifications: list[str] = field(default_factory=list)
    assigned_flights: list[Flight] = field(default_factory=list)

    def assign_to_flight(self, flight: Flight) -> None:
        if flight not in self.assigned_flights:
            self.assigned_flights.append(flight)

    def count_certifications(self) -> int:
        return len(self.certifications)
