from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SupplyOrder:
    order_id: str
    department: "Department"
    items: list[str] = field(default_factory=list)
    status: str = "pending"
    total_cost: float = 0.0

    def add_item(self, item: str, cost: float) -> None:
        self.items.append(item)
        self.total_cost += cost

    def mark_received(self) -> None:
        self.status = "received"
