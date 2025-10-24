from __future__ import annotations

from dataclasses import dataclass

from hospital.exceptions.SurgeryScheduleException import SurgeryScheduleException


@dataclass
class SurgerySchedule:
    surgery_id: str
    patient: "Patient"
    surgeon: "Surgeon"
    room: "Room"
    schedule: "Schedule"
    status: str = "pending"

    def mark_completed(self) -> None:
        self.status = "completed"

    def ensure_room_prepared(self, is_ready: bool) -> None:
        if not is_ready:
            raise SurgeryScheduleException("Operating room not prepared for surgery.")
