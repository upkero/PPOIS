from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Patient:
    patient_id: str
    name: str
    date_of_birth: str
    contact_number: str
    primary_doctor: "Doctor | None" = None
    allergies: list["Allergy"] = field(default_factory=list)
    prescriptions: list["Prescription"] = field(default_factory=list)

    def assign_doctor(self, doctor: "Doctor") -> None:
        self.primary_doctor = doctor

    def add_allergy(self, allergy: "Allergy") -> None:
        self.allergies.append(allergy)
