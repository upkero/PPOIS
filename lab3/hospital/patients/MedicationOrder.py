from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MedicationOrder:
    medication: "Medication"
    dosage: str
    frequency: str
    quantity: int

    def adjust_frequency(self, new_frequency: str) -> None:
        self.frequency = new_frequency

    def reduce_quantity(self, amount: int) -> None:
        self.quantity = max(0, self.quantity - amount)
