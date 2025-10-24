from __future__ import annotations

from dataclasses import dataclass, field

from hospital.exceptions.BillingOverdueException import BillingOverdueException


@dataclass
class BillingAccount:
    account_id: str
    patient: "Patient"
    charges: list[float] = field(default_factory=list)
    payments: list[float] = field(default_factory=list)
    insurance_policy: "InsurancePolicy | None" = None

    def add_charge(self, amount: float) -> None:
        self.charges.append(amount)

    def record_payment(self, amount: float) -> None:
        self.payments.append(amount)

    def verify_balance(self) -> float:
        balance = sum(self.charges) - sum(self.payments)
        if balance > 1000:
            raise BillingOverdueException(f"Outstanding balance is {balance:.2f}")
        return balance
