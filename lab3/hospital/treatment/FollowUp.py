from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FollowUp:
    follow_up_id: str
    patient: "Patient"
    scheduled_with: "Doctor"
    schedule: "Schedule"
    notes: str = ""

    def update_notes(self, notes: str) -> None:
        self.notes = notes

    def postpone(self, new_schedule: "Schedule") -> None:
        self.schedule = new_schedule
