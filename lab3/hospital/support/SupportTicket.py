from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SupportTicket:
    ticket_id: str
    submitted_by: str
    category: str
    description: str
    updates: list[str] = field(default_factory=list)
    status: str = "open"

    def add_update(self, update: str) -> None:
        self.updates.append(update)

    def close(self) -> None:
        self.status = "closed"
