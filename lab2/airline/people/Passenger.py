from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Passenger:
    name: str
    loyalty_id: str | None = None
    tickets: list[Ticket] = field(default_factory=list)
    luggage: list[Luggage] = field(default_factory=list)
    documents: list[TravelDocument] = field(default_factory=list)

    def add_ticket(self, ticket: Ticket) -> None:
        if ticket not in self.tickets:
            self.tickets.append(ticket)

    def add_luggage(self, bag: Luggage) -> None:
        self.luggage.append(bag)
