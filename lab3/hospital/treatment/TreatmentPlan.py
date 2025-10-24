from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TreatmentPlan:
    plan_id: str
    patient: "Patient"
    primary_doctor: "Doctor"
    procedures: list["Procedure"] = field(default_factory=list)
    therapy_sessions: list["TherapySession"] = field(default_factory=list)

    def add_procedure(self, procedure: "Procedure") -> None:
        self.procedures.append(procedure)

    def attach_therapy(self, session: "TherapySession") -> None:
        self.therapy_sessions.append(session)
