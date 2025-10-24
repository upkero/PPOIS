from __future__ import annotations

from dataclasses import dataclass, field

from airline.exceptions.FlightCancelledException import FlightCancelledException
from airline.exceptions.FlightOverbookedException import FlightOverbookedException
from airline.support.DelayReport import DelayReport


@dataclass
class Flight:
    number: str
    route: Route
    aircraft: Aircraft
    status: FlightStatus
    schedule: Schedule | None = None
    passengers: list[Passenger] = field(default_factory=list)
    crew: list[CrewMember] = field(default_factory=list)
    delay_reports: list[DelayReport] = field(default_factory=list)
    airline: Airline | None = None
    cancelled: bool = False

    def assign_airline(self, airline: Airline) -> None:
        self.airline = airline

    def board_passenger(self, passenger: Passenger) -> None:
        if self.cancelled:
            raise FlightCancelledException(f"Flight {self.number} is cancelled.")
        if len(self.passengers) >= self.aircraft.capacity:
            raise FlightOverbookedException(f"Flight {self.number} is overbooked.")
        self.passengers.append(passenger)

    def report_delay(self, minutes: int, reason: str, reporter: str) -> DelayReport:
        report = DelayReport(flight=self, minutes=minutes, reason=reason, reported_by=reporter)
        self.delay_reports.append(report)
        self.status.mark_delayed(reason)
        return report
