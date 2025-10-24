from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Cabin:
    cabin_class: str
    seats: list[Seat] = field(default_factory=list)
    crew: list[CrewMember] = field(default_factory=list)
    amenities: list[str] = field(default_factory=list)

    def assign_crew_member(self, crew_member: CrewMember) -> None:
        if crew_member not in self.crew:
            self.crew.append(crew_member)

    def available_seats(self) -> int:
        return sum(1 for seat in self.seats if seat.is_available)
