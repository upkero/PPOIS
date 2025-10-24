from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CheckInSession:
    session_id: str
    booking: Booking
    opened_by: str
    assigned_counter: str | None = None
    completed: bool = False

    def assign_counter(self, counter_id: str) -> None:
        self.assigned_counter = counter_id

    def mark_completed(self) -> None:
        self.completed = True
