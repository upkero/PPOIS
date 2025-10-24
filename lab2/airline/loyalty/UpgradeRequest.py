from __future__ import annotations

from dataclasses import dataclass


@dataclass
class UpgradeRequest:
    passenger: Passenger
    flight: Flight
    requested_tier: str
    status: str = "pending"

    def approve(self) -> None:
        self.status = "approved"

    def mark_waitlisted(self) -> None:
        self.status = "waitlisted"
