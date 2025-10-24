from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.BedUnavailableException import BedUnavailableException


@dataclass
class Ward:
    code: str
    specialty: str
    rooms: list["Room"] = field(default_factory=list)
    head_nurse: "Nurse | None" = None

    def assign_head_nurse(self, nurse: "Nurse") -> None:
        self.head_nurse = nurse

    def allocate_bed(self) -> "Bed":
        for room in self.rooms:
            bed = room.find_available_bed()
            if bed:
                return bed
        raise BedUnavailableException(f"No available beds in ward {self.code}.")
