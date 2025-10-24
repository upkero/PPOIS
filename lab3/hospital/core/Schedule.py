from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Schedule:
    start: datetime
    end: datetime
    location: str
    notes: str = ""

    def reschedule(self, new_start: datetime, new_end: datetime) -> None:
        self.start = new_start
        self.end = new_end

    def overlaps_with(self, other: "Schedule") -> bool:
        return self.start < other.end and other.start < self.end
