from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Meal:
    meal_name: str
    calories: int
    diet_type: str

    def is_suitable_for(self, diet: str) -> bool:
        return self.diet_type.lower() in {"any", diet.lower()}

    def describe(self) -> str:
        return f"{self.meal_name} ({self.diet_type})"
