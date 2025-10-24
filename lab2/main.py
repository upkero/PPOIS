from __future__ import annotations

from datetime import datetime

from airline.booking.BoardingPass import BoardingPass
from airline.booking.Booking import Booking
from airline.booking.Reservation import Reservation
from airline.booking.Ticket import Ticket
from airline.core.Aircraft import Aircraft
from airline.core.Airline import Airline
from airline.core.Airport import Airport
from airline.core.Flight import Flight
from airline.core.FlightPlan import FlightPlan
from airline.core.FlightStatus import FlightStatus
from airline.core.Route import Route
from airline.core.Schedule import Schedule
from airline.loyalty.LoyaltyMember import LoyaltyMember
from airline.loyalty.LoyaltyProgram import LoyaltyProgram
from airline.loyalty.Reward import Reward
from airline.loyalty.UpgradeRequest import UpgradeRequest
from airline.operations.Cabin import Cabin
from airline.operations.CateringOrder import CateringOrder
from airline.operations.Gate import Gate
from airline.operations.MaintenanceRecord import MaintenanceRecord
from airline.operations.Meal import Meal
from airline.operations.Seat import Seat
from airline.operations.Terminal import Terminal
from airline.operations.WeatherReport import WeatherReport
from airline.people.CrewMember import CrewMember
from airline.people.Passenger import Passenger
from airline.safety.EmergencyProcedure import EmergencyProcedure
from airline.safety.SafetyInspection import SafetyInspection
from airline.security.BoardingQueue import BoardingQueue
from airline.security.Luggage import Luggage
from airline.security.SecurityCheck import SecurityCheck
from airline.support.CustomerSupportCase import CustomerSupportCase
from airline.support.DelayReport import DelayReport
from airline.support.VIPLounge import VIPLounge
from airline.travel.TravelDocument import TravelDocument
from airline.travel.Visa import Visa


def run_demo() -> None:
    loyalty_program = LoyaltyProgram(name="SkyHigh Rewards")
    reward = Reward(reward_id="RW001", description="Lounge Access", required_points=5000)

    airline = Airline(name="SkyHigh Airlines", iata_code="SH", loyalty_program=loyalty_program)
    origin = Airport(name="Vnukovo", city="Moscow")
    destination = Airport(name="Pulkovo", city="Saint Petersburg")

    terminal_a = Terminal(name="Terminal A", airport=origin)
    gate_a5 = Gate(gate_number="A5", terminal=terminal_a)
    terminal_a.add_gate(gate_a5)
    origin.terminals.append(terminal_a)
    origin.gates.append(gate_a5)

    aircraft = Aircraft(registration="RA-82045", model="Sukhoi Superjet", capacity=100)
    airline.fleet.append(aircraft)

    flight_status = FlightStatus(code="ON_TIME", description="Scheduled departure", last_updated=datetime.now())
    route = Route(origin=origin, destination=destination, distance_km=650)
    flight_plan = FlightPlan(route=route, cruising_altitude_ft=32000, fuel_required_kg=5400.0)
    flight_plan.add_weather_note("Clear skies expected")
    schedule = Schedule(
        departure_time=datetime(2025, 6, 10, 9, 30),
        arrival_time=datetime(2025, 6, 10, 11, 20),
    )
    schedule.assign_gate(gate=gate_a5, terminal=terminal_a)

    flight = Flight(
        number="SH123",
        route=route,
        aircraft=aircraft,
        status=flight_status,
        schedule=schedule,
    )
    airline.add_flight(flight)

    cabin = Cabin(cabin_class="Business")
    seat_1a = Seat(seat_number="1A", cabin_class="Business")
    seat_1b = Seat(seat_number="1B", cabin_class="Business")
    cabin.seats.extend([seat_1a, seat_1b])

    captain = CrewMember(name="Irina Volkova", role="Captain")
    first_officer = CrewMember(name="Dmitry Smirnov", role="First Officer")
    cabin.assign_crew_member(captain)
    cabin.assign_crew_member(first_officer)
    captain.assign_to_flight(flight)
    first_officer.assign_to_flight(flight)
    flight.crew.extend([captain, first_officer])

    passenger = Passenger(name="Sofia Petrova", loyalty_id="LP1001")
    travel_doc = TravelDocument(document_type="Passport", number="AB1234567", expiry_date="2030-12-31", passenger=passenger)
    visa = Visa(country="Russia", valid_until="2026-12-31", entries_allowed=2, linked_document=travel_doc)
    passenger.documents.append(travel_doc)
    visa.consume_entry()

    booking = Booking(reference="BK20250610")
    booking.add_passenger(passenger)
    booking.add_flight(flight, price=350.0)
    booking.process_payment(amount=350.0)

    reservation = Reservation(identifier="RS123", booking=booking)
    reservation.add_seat_request(passenger_name=passenger.name, preference="window")
    reservation.confirm()

    ticket = Ticket(ticket_number="TCK123", passenger=passenger, flight=flight)
    passenger.add_ticket(ticket)
    ticket.assign_seat(seat_1a)
    ticket.mark_status("checked_in")
    flight.board_passenger(passenger)

    boarding_pass = BoardingPass(barcode="QR-SH123-1A", ticket=ticket, gate=gate_a5, boarding_zone="Priority")

    queue = BoardingQueue(flight=flight)
    queue.enqueue_passenger(passenger)
    next_for_boarding = queue.next_passenger()

    luggage = Luggage(weight=18.0, owner=passenger)
    passenger.add_luggage(luggage)
    luggage.ensure_weight_limit(limit=23.0)

    security_check = SecurityCheck(checkpoint_id="S1", airport=origin)
    security_check.add_to_queue(passenger)
    security_check.confiscate_item("umbrella")

    vip_lounge = VIPLounge(lounge_name="SkyHigh Elite Lounge", airport=origin, capacity=50)
    loyalty_member = LoyaltyMember(passenger=passenger, tier="Silver", points=6000)
    loyalty_member.rewards.append(reward)
    loyalty_program.register_member(loyalty_member)
    loyalty_member.attempt_tier_upgrade("Gold")
    vip_access_granted = vip_lounge.admit_guest(passenger)

    upgrade_request = UpgradeRequest(passenger=passenger, flight=flight, requested_tier="Business")
    upgrade_request.approve()

    catering_order = CateringOrder(order_id="CT123", flight=flight)
    catering_order.add_meal(Meal(meal_name="Salmon Fillet", calories=540, diet_type="Any"))
    catering_order.dispatch()

    maintenance_record = MaintenanceRecord(
        record_id="MR001",
        aircraft=aircraft,
        description="Hydraulic system inspection",
        completed=True,
        reported_by="Technician Team",
    )
    aircraft.maintenance_records.append(maintenance_record)
    aircraft.require_recent_maintenance()

    weather_report = WeatherReport(airport=origin, condition="Clear", temperature_c=18.5, wind_speed=12.0)
    is_takeoff_safe = weather_report.is_safe_for_takeoff()

    delay_report: DelayReport | None = None
    if not is_takeoff_safe:
        delay_report = flight.report_delay(minutes=45, reason="Weather Hold", reporter="Dispatch")

    emergency_procedure = EmergencyProcedure(procedure_code="EM-001", description="Cabin depressurization")
    emergency_procedure.required_roles.extend(["Captain", "Flight Attendant"])
    emergency_procedure.schedule_drill(date="2025-05-05")

    safety_inspection = SafetyInspection(inspection_id="SI-2025-05", inspector="CAA Specialist")
    safety_inspection.add_finding("Life jackets validated")
    safety_inspection.close()

    support_case = CustomerSupportCase(
        case_id="CS-0001",
        passenger=passenger,
        complaint="Request for vegetarian meal confirmation",
    )
    support_case.assign_agent("Elena Morozova")
    support_case.close()

    boarding_pass_verified = boarding_pass.verify_passenger(passenger)

    print("=== Airline Demonstration Scenario ===")
    print(f"Airline: {airline.name}, Total Capacity: {airline.calculate_total_capacity()} seats")
    print(f"Flight {flight.number} from {route.origin.city} to {route.destination.city} with {len(flight.passengers)} passenger(s)")
    print(f"Loyalty tier for {passenger.name}: {loyalty_member.tier}, VIP lounge admitted: {vip_access_granted}")
    print(f"Seat {seat_1a.seat_number} assigned to: {seat_1a.passenger.name if seat_1a.passenger else 'None'}")
    print(f"Next in boarding queue: {next_for_boarding.name if next_for_boarding else 'No passengers'}")
    print(f"Security confiscated items: {security_check.confiscated_items}")
    print(f"Catering status: {catering_order.status} with {len(catering_order.meals)} meal(s)")
    print(f"Weather safe for takeoff: {is_takeoff_safe}")
    print(f"Flight plan notes: {', '.join(flight_plan.weather_notes)}")
    print(f"Delay reported: {delay_report.summary() if delay_report else 'No delay'}")
    print(f"Emergency procedure last drill: {emergency_procedure.last_drilled}")
    print(f"Safety inspection status: {safety_inspection.status}")
    print(f"Boarding pass verified: {boarding_pass_verified}")


if __name__ == "__main__":
    run_demo()
