from __future__ import annotations

from dataclasses import dataclass, field

from airline.exceptions.PaymentDeclinedException import PaymentDeclinedException


@dataclass
class Booking:
    reference: str
    passengers: list[Passenger] = field(default_factory=list)
    flights: list[Flight] = field(default_factory=list)
    total_price: float = 0.0
    payments: list[float] = field(default_factory=list)

    def add_passenger(self, passenger: Passenger) -> None:
        if passenger not in self.passengers:
            self.passengers.append(passenger)

    def add_flight(self, flight: Flight, price: float) -> None:
        if flight not in self.flights:
            self.flights.append(flight)
            self.total_price += price

    def average_price_per_passenger(self) -> float:
        if not self.passengers:
            return 0.0
        return round(self.total_price / len(self.passengers), 2)

    def process_payment(self, amount: float) -> None:
        if amount <= 0:
            raise PaymentDeclinedException("Payment must be positive.")
        if amount + sum(self.payments) < self.total_price:
            raise PaymentDeclinedException("Insufficient payment for booking.")
        self.payments.append(amount)
