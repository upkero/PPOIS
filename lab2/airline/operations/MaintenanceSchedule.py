from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MaintenanceSchedule:
    schedule_id: str
    aircraft: Aircraft
    due_date: str
    tasks: list[str] = field(default_factory=list)

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

    def postpone(self, new_date: str) -> None:
        self.due_date = new_date
