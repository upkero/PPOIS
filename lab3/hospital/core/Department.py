from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Department:
    name: str
    floor: int
    head: StaffMember | None = None
    staff: list[StaffMember] = field(default_factory=list)
    wards: list["Ward"] = field(default_factory=list)

    def assign_head(self, staff_member: StaffMember) -> None:
        self.head = staff_member

    def add_staff_member(self, staff_member: StaffMember) -> None:
        if staff_member not in self.staff:
            self.staff.append(staff_member)
