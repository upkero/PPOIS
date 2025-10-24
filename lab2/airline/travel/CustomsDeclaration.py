from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CustomsDeclaration:
    passenger: Passenger
    items: list[str] = field(default_factory=list)
    total_value: float = 0.0
    declared_currency: str = "USD"

    def add_item(self, item: str, value: float) -> None:
        self.items.append(item)
        self.total_value += value

    def requires_inspection(self, threshold: float = 1000.0) -> bool:
        restricted = {"weapons", "livestock"}
        return self.total_value > threshold or any(item in restricted for item in self.items)
