from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SecurityIncident:
    incident_id: str
    reported_by: "StaffMember"
    description: str
    occurred_at: datetime
    involved_persons: list[str] = field(default_factory=list)
    resolved: bool = False

    def add_person(self, person: str) -> None:
        if person not in self.involved_persons:
            self.involved_persons.append(person)

    def mark_resolved(self) -> None:
        self.resolved = True
