from __future__ import annotations

from dataclasses import dataclass

from airline.exceptions.VisaInvalidException import VisaInvalidException


@dataclass
class Visa:
    country: str
    valid_until: str
    entries_allowed: int
    linked_document: TravelDocument

    def consume_entry(self) -> None:
        if self.entries_allowed <= 0:
            raise VisaInvalidException(f"No entries left for {self.country}.")
        self.entries_allowed -= 1

    def is_valid_on(self, date_str: str) -> bool:
        return self.valid_until >= date_str
