from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CompensationClaim:
    claim_id: str
    passenger: Passenger
    reason: str
    amount: float
    status: str = "filed"

    def escalate(self) -> None:
        self.status = "escalated"

    def settle(self, payout: float) -> float:
        self.status = "settled"
        return payout
