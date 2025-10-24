from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.EquipmentMaintenanceException import EquipmentMaintenanceException


@dataclass
class Equipment:
    equipment_id: str
    name: str
    department: "Department"
    maintenance_logs: list[str] = field(default_factory=list)
    operational: bool = True

    def add_maintenance_log(self, entry: str) -> None:
        self.maintenance_logs.append(entry)

    def mark_operational(self, status: bool) -> None:
        self.operational = status
        if not status:
            raise EquipmentMaintenanceException(f"Equipment {self.equipment_id} is out of service.")
