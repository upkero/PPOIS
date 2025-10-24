from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CareTask:
    task_id: str
    description: str
    assigned_nurse: "Nurse"
    patient: "Patient"
    completed: bool = False

    def mark_completed(self) -> None:
        self.completed = True

    def reassign(self, nurse: "Nurse") -> None:
        self.assigned_nurse = nurse
