from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.AppointmentConflictException import AppointmentConflictException


@dataclass
class Hospital:
    name: str
    address: str
    departments: list["Department"] = field(default_factory=list)
    wards: list["Ward"] = field(default_factory=list)
    appointments: list["Appointment"] = field(default_factory=list)

    def register_department(self, department: "Department") -> None:
        if department not in self.departments:
            self.departments.append(department)

    def schedule_appointment(self, appointment: "Appointment") -> None:
        for existing in self.appointments:
            if existing.room is appointment.room and existing.schedule.overlaps_with(appointment.schedule):
                raise AppointmentConflictException(f"Room {appointment.room.number} already booked.")
        self.appointments.append(appointment)
