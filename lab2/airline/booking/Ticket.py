from __future__ import annotations

from dataclasses import dataclass

from airline.exceptions.InvalidTicketStatusException import InvalidTicketStatusException
from airline.exceptions.SeatAlreadyAssignedException import SeatAlreadyAssignedException


@dataclass
class Ticket:
    ticket_number: str
    passenger: Passenger
    flight: Flight
    seat: Seat | None = None
    status: str = "booked"

    def assign_seat(self, seat: Seat) -> None:
        if self.seat is not None and self.seat is not seat:
            raise SeatAlreadyAssignedException(f"Ticket {self.ticket_number} already has a seat.")
        self.seat = seat
        seat.assign_passenger(self.passenger)

    def mark_status(self, new_status: str) -> None:
        valid_statuses = {"booked", "checked_in", "boarded", "cancelled"}
        if new_status not in valid_statuses:
            raise InvalidTicketStatusException(f"Status {new_status} is invalid.")
        self.status = new_status
