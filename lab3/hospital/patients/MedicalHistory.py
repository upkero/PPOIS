from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MedicalHistory:
    history_id: str
    patient: "Patient"
    past_conditions: list[str] = field(default_factory=list)
    surgeries: list[str] = field(default_factory=list)
    family_history: list[str] = field(default_factory=list)

    def add_condition(self, condition: str) -> None:
        self.past_conditions.append(condition)

    def record_surgery(self, surgery: str) -> None:
        self.surgeries.append(surgery)
