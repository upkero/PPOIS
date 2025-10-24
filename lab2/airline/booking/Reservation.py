from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Reservation:
    identifier: str
    booking: Booking
    seat_requests: dict[str, str] = field(default_factory=dict)
    status: str = "pending"

    def add_seat_request(self, passenger_name: str, preference: str) -> None:
        self.seat_requests[passenger_name] = preference

    def confirm(self) -> None:
        self.status = "confirmed"
