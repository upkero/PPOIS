from __future__ import annotations

from dataclasses import dataclass

from hospital.exceptions.InsuranceClaimDeniedException import InsuranceClaimDeniedException


@dataclass
class InsuranceClaim:
    claim_id: str
    policy: "InsurancePolicy"
    amount: float
    status: str = "submitted"
    reason: str = ""

    def approve(self) -> None:
        self.status = "approved"

    def deny(self, reason: str) -> None:
        self.status = "denied"
        self.reason = reason
        raise InsuranceClaimDeniedException(reason)
