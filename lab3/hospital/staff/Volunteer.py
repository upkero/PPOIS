from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Volunteer:
    volunteer_id: str
    name: str
    assigned_department: "Department | None" = None
    hours_logged: float = 0.0
    tasks_completed: list[str] = field(default_factory=list)

    def assign_department(self, department: "Department") -> None:
        self.assigned_department = department

    def log_hours(self, hours: float) -> None:
        self.hours_logged += hours
