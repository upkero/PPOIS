from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.MedicationOutOfStockException import MedicationOutOfStockException


@dataclass
class Pharmacist:
    staff_member: StaffMember
    managed_inventory: list["Medication"] = field(default_factory=list)
    orders_processed: list["MedicationOrder"] = field(default_factory=list)

    def add_inventory_item(self, medication: "Medication") -> None:
        if medication not in self.managed_inventory:
            self.managed_inventory.append(medication)

    def dispense_medication(self, order: "MedicationOrder") -> None:
        if order.medication not in self.managed_inventory:
            raise MedicationOutOfStockException("Medication not available in inventory.")
        self.orders_processed.append(order)
