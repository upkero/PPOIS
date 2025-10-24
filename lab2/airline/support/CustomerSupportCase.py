from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CustomerSupportCase:
    case_id: str
    passenger: Passenger
    complaint: str
    status: str = "open"
    assigned_agent: str | None = None

    def assign_agent(self, agent_name: str) -> None:
        self.assigned_agent = agent_name

    def close(self) -> None:
        self.status = "closed"
