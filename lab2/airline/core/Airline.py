from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Airline:
    name: str
    iata_code: str
    loyalty_program: LoyaltyProgram | None = None
    fleet: list[Aircraft] = field(default_factory=list)
    flights: list[Flight] = field(default_factory=list)

    def add_flight(self, flight: Flight) -> None:
        if flight not in self.flights:
            self.flights.append(flight)
            flight.assign_airline(self)

    def calculate_total_capacity(self) -> int:
        return sum(aircraft.capacity for aircraft in self.fleet)
