from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class StaffMember:
    staff_id: str
    name: str
    role: str
    department: "Department | None" = None
    shifts: list["Shift"] = field(default_factory=list)

    def assign_department(self, department: "Department") -> None:
        self.department = department

    def add_shift(self, shift: "Shift") -> None:
        self.shifts.append(shift)
