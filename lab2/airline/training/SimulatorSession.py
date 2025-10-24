from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SimulatorSession:
    session_id: str
    trainees: list[CrewMember] = field(default_factory=list)
    duration_hours: float = 0.0
    scenario: str = ""

    def add_trainee(self, crew_member: CrewMember) -> None:
        if crew_member not in self.trainees:
            self.trainees.append(crew_member)

    def describe(self) -> str:
        return f"{self.session_id} - {self.scenario} ({len(self.trainees)} trainees)"
