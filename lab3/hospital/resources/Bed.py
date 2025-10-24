from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Bed:
    bed_id: str
    ward_code: str
    is_available: bool = True
    current_patient: "Patient | None" = None

    def assign_patient(self, patient: "Patient") -> None:
        self.current_patient = patient
        self.is_available = False

    def release(self) -> None:
        self.current_patient = None
        self.is_available = True
