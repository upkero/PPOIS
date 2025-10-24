from __future__ import annotations

from dataclasses import dataclass, field

from airline.exceptions.MaintenanceOverdueException import MaintenanceOverdueException


@dataclass
class Aircraft:
    registration: str
    model: str
    capacity: int
    maintenance_records: list[MaintenanceRecord] = field(default_factory=list)
    assigned_flights: list[Flight] = field(default_factory=list)

    def assign_flight(self, flight: Flight) -> None:
        if flight not in self.assigned_flights:
            self.assigned_flights.append(flight)

    def require_recent_maintenance(self) -> None:
        if not self.maintenance_records:
            raise MaintenanceOverdueException(f"Aircraft {self.registration} has no maintenance records.")
        if not any(record.completed for record in self.maintenance_records[-3:]):
            raise MaintenanceOverdueException(f"Aircraft {self.registration} needs recent maintenance.")
