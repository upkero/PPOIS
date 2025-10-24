from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BoardingPass:
    barcode: str
    ticket: Ticket
    gate: Gate
    boarding_zone: str

    def update_gate(self, gate: Gate) -> None:
        self.gate = gate

    def verify_passenger(self, passenger: Passenger) -> bool:
        return self.ticket.passenger is passenger
