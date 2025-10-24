from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GroundCrew:
    name: str
    shift: str
    assigned_tasks: list[str] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)

    def assign_task(self, task: str) -> None:
        self.assigned_tasks.append(task)

    def has_certification(self, certificate: str) -> bool:
        return certificate in self.certifications
