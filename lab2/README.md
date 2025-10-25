Airline Domain Model
====================

Aircraft 5 2 → Flight, MaintenanceRecord
Airline 5 2 → Aircraft, Flight, LoyaltyProgram
Airport 5 2 → Flight, Gate, Runway, Terminal
BaggageTag 4 2 → Flight, Passenger
Beverage 3 2 →
BoardingPass 4 2 → Gate, Passenger, Ticket
BoardingQueue 3 2 → Flight, Passenger
Booking 5 4 → Flight, Passenger
Cabin 4 2 → CrewMember, Seat
CateringOrder 5 2 → Beverage, Flight, Meal
CheckInSession 5 2 → Booking
CompensationClaim 5 2 → Passenger
Complaint 4 2 → CustomerSupportCase, Passenger
CrewMember 4 2 → Flight
CustomerSupportCase 5 2 → Passenger
CustomsDeclaration 4 2 → Passenger
DelayReport 4 2 → Flight
DutyRoster 4 3 → CrewMember, Flight
EmergencyProcedure 4 2 →
Fleet 3 2 → Aircraft
Flight 10 3 → Aircraft, Airline, CrewMember, DelayReport, FlightStatus, Passenger, Route, Schedule
FlightPlan 4 2 → Route
FlightStatus 3 2 →
FuelReport 4 2 → Flight
Gate 4 2 → Flight, Schedule, Terminal
GroundCrew 4 2 →
LoyaltyMember 4 2 → Passenger, Reward
LoyaltyProgram 3 2 → LoyaltyMember
Luggage 4 2 → Passenger
MaintenanceRecord 5 2 → Aircraft
MaintenanceSchedule 4 2 → Aircraft
Meal 3 2 →
Passenger 5 2 → Luggage, Ticket, TravelDocument
Reservation 4 2 → Booking
Reward 3 2 →
Route 4 2 → Airport
Runway 4 2 → Flight
SafetyInspection 4 2 →
Schedule 5 2 → Gate, Terminal
Seat 4 2 → Passenger
SecurityCheck 4 2 → Airport, Passenger
SimulatorSession 4 2 → CrewMember
Terminal 4 2 → Airport, Gate
Ticket 5 2 → Flight, Passenger, Seat
TrainingCourse 4 2 → CrewMember
TravelDocument 4 2 → Passenger
UpgradeRequest 4 2 → Flight, Passenger
VIPLounge 4 2 → Airport, Passenger
Visa 4 2 → TravelDocument
WeatherReport 4 2 → Airport

Exceptions (12):
----------------

CateringItemMissingException 0 1 →
FlightCancelledException 0 1 →
FlightOverbookedException 0 1 →
InvalidTicketStatusException 0 1 →
LoyaltyTierUpgradeException 0 1 →
LuggageOverweightException 0 1 →
MaintenanceOverdueException 0 1 →
PaymentDeclinedException 0 1 →
SeatAlreadyAssignedException 0 1 →
SecurityAlertException 0 1 →
UnauthorizedAccessException 0 1 →
VisaInvalidException 0 1 →

Итоги
-----

Поля: 211
Поведения: 116
Ассоциации: 78
Исключения: 12

