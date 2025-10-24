from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Visit:
    visit_id: str
    patient: "Patient"
    doctor: "Doctor"
    visit_time: datetime
    notes: list[str] = field(default_factory=list)

    def add_note(self, note: str) -> None:
        self.notes.append(note)

    def summarize(self) -> str:
        return f"Visit {self.visit_id} with {self.doctor.name} at {self.visit_time.isoformat()}"
