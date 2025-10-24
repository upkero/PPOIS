from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MealPlan:
    plan_id: str
    patient: "Patient"
    caloric_target: int
    meals: list[str] = field(default_factory=list)
    restrictions: list[str] = field(default_factory=list)

    def add_meal(self, meal: str) -> None:
        self.meals.append(meal)

    def add_restriction(self, restriction: str) -> None:
        if restriction not in self.restrictions:
            self.restrictions.append(restriction)
