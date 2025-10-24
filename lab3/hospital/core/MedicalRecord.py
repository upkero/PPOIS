from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MedicalRecord:
    record_id: str
    patient: "Patient"
    diagnoses: list["Diagnosis"] = field(default_factory=list)
    visits: list["Visit"] = field(default_factory=list)

    def add_diagnosis(self, diagnosis: "Diagnosis") -> None:
        self.diagnoses.append(diagnosis)

    def log_visit(self, visit: "Visit") -> None:
        self.visits.append(visit)
