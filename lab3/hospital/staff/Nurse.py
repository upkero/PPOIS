from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Nurse:
    staff_member: StaffMember
    certifications: list[str] = field(default_factory=list)
    assigned_ward: "Ward | None" = None
    patients_in_care: list["Patient"] = field(default_factory=list)

    def add_certification(self, certification: str) -> None:
        self.certifications.append(certification)

    def assign_patient_care(self, patient: "Patient") -> None:
        if patient not in self.patients_in_care:
            self.patients_in_care.append(patient)
