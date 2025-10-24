from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Doctor:
    staff_member: StaffMember
    specialties: list[str] = field(default_factory=list)
    active_patients: list["Patient"] = field(default_factory=list)
    license_number: str = ""

    def add_specialty(self, specialty: str) -> None:
        if specialty not in self.specialties:
            self.specialties.append(specialty)

    def assign_patient(self, patient: "Patient") -> None:
        if patient not in self.active_patients:
            self.active_patients.append(patient)
