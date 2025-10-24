from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MaintenanceRecord:
    record_id: str
    aircraft: Aircraft
    description: str
    completed: bool
    reported_by: str

    def mark_completed(self) -> None:
        self.completed = True

    def summary(self) -> str:
        status = "done" if self.completed else "pending"
        return f"{self.record_id} - {status}: {self.description}"
