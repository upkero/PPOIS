from __future__ import annotations

from dataclasses import dataclass

from hospital.exceptions.PatientNotFoundException import PatientNotFoundException


@dataclass
class Appointment:
    identifier: str
    patient: "Patient"
    doctor: "Doctor"
    room: "Room"
    schedule: "Schedule"
    status: str = "scheduled"

    def confirm(self) -> None:
        self.status = "confirmed"

    def verify_patient_identity(self, patient_id: str) -> None:
        if patient_id != self.patient.patient_id:
            raise PatientNotFoundException("Provided patient identifier does not match appointment record.")
