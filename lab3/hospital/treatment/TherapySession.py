from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TherapySession:
    session_id: str
    patient: "Patient"
    therapist: "Therapist"
    schedule: "Schedule"
    session_type: str

    def reschedule(self, new_schedule: "Schedule") -> None:
        self.schedule = new_schedule

    def describe(self) -> str:
        return f"{self.session_type} session for {self.patient.name}"
