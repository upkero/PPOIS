from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrainingCourse:
    course_id: str
    title: str
    enrolled_members: list[CrewMember] = field(default_factory=list)
    passing_score: int = 80

    def enroll_member(self, crew_member: CrewMember) -> None:
        if crew_member not in self.enrolled_members:
            self.enrolled_members.append(crew_member)

    def has_passed(self, score: int) -> bool:
        return score >= self.passing_score
