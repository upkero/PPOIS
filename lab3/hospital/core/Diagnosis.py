from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Diagnosis:
    code: str
    description: str
    diagnosed_by: "Doctor"
    symptoms: list[str] = field(default_factory=list)
    severity: str = "moderate"

    def add_symptom(self, symptom: str) -> None:
        if symptom not in self.symptoms:
            self.symptoms.append(symptom)

    def is_critical(self) -> bool:
        return self.severity.lower() in {"critical", "severe"}
