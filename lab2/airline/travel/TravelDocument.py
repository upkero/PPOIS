from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TravelDocument:
    document_type: str
    number: str
    expiry_date: str
    passenger: Passenger

    def is_valid_on(self, date_str: str) -> bool:
        return self.expiry_date >= date_str

    def masked_number(self) -> str:
        return f"{self.number[:2]}***{self.number[-2:]}"
