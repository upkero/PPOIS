from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RehabilitationPlan:
    plan_id: str
    patient: "Patient"
    therapist: "Therapist"
    goals: list[str] = field(default_factory=list)
    progress_notes: list[str] = field(default_factory=list)

    def add_goal(self, goal: str) -> None:
        self.goals.append(goal)

    def record_progress(self, note: str) -> None:
        self.progress_notes.append(note)
