from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Complaint:
    passenger: Passenger
    message: str
    severity: int
    linked_case: CustomerSupportCase | None = None

    def escalate(self) -> None:
        self.severity = min(self.severity + 1, 5)

    def link_case(self, case: CustomerSupportCase) -> None:
        self.linked_case = case
