from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.MedicationOutOfStockException import MedicationOutOfStockException


@dataclass
class Prescription:
    prescription_id: str
    patient: "Patient"
    prescribed_by: "Doctor"
    medications: list["MedicationOrder"] = field(default_factory=list)
    status: str = "active"

    def add_medication(self, order: "MedicationOrder") -> None:
        if order.quantity <= 0:
            raise MedicationOutOfStockException("Medication quantity must be positive.")
        self.medications.append(order)

    def deactivate(self) -> None:
        self.status = "inactive"
