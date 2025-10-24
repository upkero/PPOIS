from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Receptionist:
    staff_member: StaffMember
    desks_managed: list[str] = field(default_factory=list)
    scheduled_appointments: list["Appointment"] = field(default_factory=list)

    def add_desk(self, desk_name: str) -> None:
        if desk_name not in self.desks_managed:
            self.desks_managed.append(desk_name)

    def register_appointment(self, appointment: "Appointment") -> None:
        self.scheduled_appointments.append(appointment)
