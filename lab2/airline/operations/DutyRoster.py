from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DutyRoster:
    roster_id: str
    crew_members: list[CrewMember] = field(default_factory=list)
    date: str = ""
    assigned_flights: list[Flight] = field(default_factory=list)

    def add_crew_member(self, member: CrewMember) -> None:
        if member not in self.crew_members:
            self.crew_members.append(member)

    def assign_flight(self, flight: Flight) -> None:
        if flight not in self.assigned_flights:
            self.assigned_flights.append(flight)

    def flights_for_member(self, member: CrewMember) -> int:
        return sum(1 for flight in self.assigned_flights if member in flight.crew)
