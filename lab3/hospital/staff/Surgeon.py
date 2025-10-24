from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.SurgeryScheduleException import SurgeryScheduleException


@dataclass
class Surgeon:
    staff_member: StaffMember
    operating_rooms: list["Room"] = field(default_factory=list)
    scheduled_surgeries: list["SurgerySchedule"] = field(default_factory=list)

    def assign_operating_room(self, room: "Room") -> None:
        if room not in self.operating_rooms:
            self.operating_rooms.append(room)

    def add_surgery(self, surgery: "SurgerySchedule") -> None:
        if surgery in self.scheduled_surgeries:
            raise SurgeryScheduleException("Surgery already scheduled for this surgeon.")
        self.scheduled_surgeries.append(surgery)
