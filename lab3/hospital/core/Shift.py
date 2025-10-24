from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Shift:
    code: str
    schedule: "Schedule"
    assigned_staff: list[StaffMember] = field(default_factory=list)
    supervisor: StaffMember | None = None

    def assign_staff(self, staff_member: StaffMember) -> None:
        if staff_member not in self.assigned_staff:
            self.assigned_staff.append(staff_member)

    def set_supervisor(self, staff_member: StaffMember) -> None:
        self.supervisor = staff_member
