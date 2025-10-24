from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class EmergencyProcedure:
    procedure_code: str
    description: str
    required_roles: list[str] = field(default_factory=list)
    last_drilled: str = ""

    def schedule_drill(self, date: str) -> None:
        self.last_drilled = date

    def requires_role(self, role: str) -> bool:
        return role in self.required_roles
