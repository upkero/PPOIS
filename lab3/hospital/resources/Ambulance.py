from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Ambulance:
    vehicle_id: str
    crew: list["StaffMember"] = field(default_factory=list)
    status: str = "available"
    assigned_calls: list[str] = field(default_factory=list)

    def dispatch(self, call_id: str) -> None:
        self.status = "on_call"
        self.assigned_calls.append(call_id)

    def mark_available(self) -> None:
        self.status = "available"
