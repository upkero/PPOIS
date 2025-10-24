from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DelayReport:
    flight: Flight
    minutes: int
    reason: str
    reported_by: str

    def extend_delay(self, additional: int) -> None:
        self.minutes += additional

    def summary(self) -> str:
        return f"{self.flight.number} delayed by {self.minutes} minutes: {self.reason}"
