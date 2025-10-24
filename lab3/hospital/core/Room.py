from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Room:
    number: str
    level: int
    beds: list["Bed"] = field(default_factory=list)
    assigned_patients: list["Patient"] = field(default_factory=list)

    def find_available_bed(self) -> "Bed | None":
        for bed in self.beds:
            if bed.is_available:
                return bed
        return None

    def admit_patient(self, patient: "Patient") -> None:
        bed = self.find_available_bed()
        if bed:
            bed.assign_patient(patient)
            self.assigned_patients.append(patient)
