import pytest

from airline.booking.Booking import Booking
from airline.exceptions.PaymentDeclinedException import PaymentDeclinedException
from airline.people.Passenger import Passenger


def test_add_passenger_adds_only_unique_entries():
    booking = Booking(reference="ABC123")
    passenger = Passenger(name="John Doe")

    booking.add_passenger(passenger)
    booking.add_passenger(passenger)

    assert booking.passengers == [passenger]


def test_add_flight_updates_total_price_once_per_flight():
    booking = Booking(reference="ABC123")
    flight = object()

    booking.add_flight(flight, 120.5)
    booking.add_flight(flight, 99.9)

    assert booking.flights == [flight]
    assert booking.total_price == pytest.approx(120.5)


def test_average_price_per_passenger_handles_no_passengers():
    booking = Booking(reference="ABC123")

    assert booking.average_price_per_passenger() == 0.0


def test_average_price_per_passenger_returns_rounded_value():
    booking = Booking(reference="ABC123")
    passengers = [Passenger(name="Alice"), Passenger(name="Bob")]
    for passenger in passengers:
        booking.add_passenger(passenger)

    booking.add_flight("FL100", 120.0)
    booking.add_flight("FL200", 180.0)

    assert booking.average_price_per_passenger() == 150.0


def test_process_payment_rejects_non_positive_amount():
    booking = Booking(reference="ABC123")
    booking.total_price = 200.0

    with pytest.raises(PaymentDeclinedException):
        booking.process_payment(0)


def test_process_payment_rejects_insufficient_amount():
    booking = Booking(reference="ABC123")
    booking.total_price = 300.0

    with pytest.raises(PaymentDeclinedException):
        booking.process_payment(299.99)


def test_process_payment_appends_valid_payment():
    booking = Booking(reference="ABC123")
    booking.total_price = 200.0

    booking.process_payment(250.0)

    assert booking.payments == [250.0]
