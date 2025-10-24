from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Medication:
    medication_id: str
    name: str
    form: str
    stock_level: int

    def restock(self, amount: int) -> None:
        self.stock_level += amount

    def consume(self, amount: int) -> None:
        self.stock_level = max(0, self.stock_level - amount)
