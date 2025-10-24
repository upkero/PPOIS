from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.UnauthorizedAccessException import UnauthorizedAccessException


@dataclass
class PatientPortalAccount:
    username: str
    patient: "Patient"
    password_hash: str
    linked_records: list[str] = field(default_factory=list)

    def link_record(self, record_id: str) -> None:
        if record_id not in self.linked_records:
            self.linked_records.append(record_id)

    def verify_access(self, provided_hash: str) -> None:
        if provided_hash != self.password_hash:
            raise UnauthorizedAccessException("Invalid portal credentials.")
