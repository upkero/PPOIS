from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DischargeSummary:
    summary_id: str
    patient: "Patient"
    attending_doctor: "Doctor"
    recommendations: list[str] = field(default_factory=list)
    follow_up_schedule: "Schedule | None" = None

    def add_recommendation(self, recommendation: str) -> None:
        self.recommendations.append(recommendation)

    def set_follow_up(self, schedule: "Schedule") -> None:
        self.follow_up_schedule = schedule
