from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.TrainingRequirementException import TrainingRequirementException


@dataclass
class Administrator:
    staff_member: StaffMember
    managed_departments: list["Department"] = field(default_factory=list)
    compliance_tasks: list[str] = field(default_factory=list)
    completed_trainings: list[str] = field(default_factory=list)

    def assign_department(self, department: "Department") -> None:
        if department not in self.managed_departments:
            self.managed_departments.append(department)

    def verify_training(self, training_code: str) -> None:
        if training_code not in self.completed_trainings:
            raise TrainingRequirementException(f"Administrator missing training {training_code}.")
