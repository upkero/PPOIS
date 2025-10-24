from __future__ import annotations

from dataclasses import dataclass, field

from airline.exceptions.CateringItemMissingException import CateringItemMissingException


@dataclass
class CateringOrder:
    order_id: str
    flight: Flight
    meals: list[Meal] = field(default_factory=list)
    beverages: list[Beverage] = field(default_factory=list)
    status: str = "pending"

    def add_meal(self, meal: Meal) -> None:
        self.meals.append(meal)

    def dispatch(self) -> None:
        if not self.meals and not self.beverages:
            raise CateringItemMissingException("Cannot dispatch empty catering order.")
        self.status = "dispatched"
