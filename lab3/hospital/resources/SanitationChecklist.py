from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.InfectionControlBreachException import InfectionControlBreachException


@dataclass
class SanitationChecklist:
    checklist_id: str
    ward: "Ward"
    tasks: list[str] = field(default_factory=list)
    completed_tasks: list[str] = field(default_factory=list)

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

    def complete_task(self, task: str) -> None:
        if task in self.tasks and task not in self.completed_tasks:
            self.completed_tasks.append(task)

    def verify_completion(self) -> None:
        if set(self.tasks) != set(self.completed_tasks):
            raise InfectionControlBreachException("Sanitation checklist incomplete.")
