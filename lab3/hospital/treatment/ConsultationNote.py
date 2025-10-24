from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConsultationNote:
    note_id: str
    doctor: "Doctor"
    patient: "Patient"
    content: str
    created_on: str

    def append_content(self, additional: str) -> None:
        self.content += f"\n{additional}"

    def preview(self) -> str:
        return self.content[:50]

