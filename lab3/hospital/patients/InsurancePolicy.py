from __future__ import annotations

from dataclasses import dataclass


@dataclass
class InsurancePolicy:
    policy_number: str
    provider: str
    coverage_limit: float
    expiry_date: str

    def is_active(self, current_date: str) -> bool:
        return current_date <= self.expiry_date

    def remaining_coverage(self, used_amount: float) -> float:
        return max(0.0, self.coverage_limit - used_amount)
