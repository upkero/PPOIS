from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Therapist:
    staff_member: StaffMember
    focus_area: str
    active_sessions: list["TherapySession"] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)

    def schedule_session(self, session: "TherapySession") -> None:
        self.active_sessions.append(session)

    def add_certification(self, certification: str) -> None:
        if certification not in self.certifications:
            self.certifications.append(certification)
