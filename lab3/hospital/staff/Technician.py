from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Technician:
    staff_member: StaffMember
    specialty: str
    assigned_equipment: list["Equipment"] = field(default_factory=list)
    completed_tasks: list[str] = field(default_factory=list)

    def assign_equipment(self, equipment: "Equipment") -> None:
        if equipment not in self.assigned_equipment:
            self.assigned_equipment.append(equipment)

    def record_task(self, task_description: str) -> None:
        self.completed_tasks.append(task_description)
