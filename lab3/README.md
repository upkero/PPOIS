Hospital Domain Model
=====================

Administrator 4 2 → Department, StaffMember
Allergy 3 2 →
Ambulance 4 2 → StaffMember
Appointment 6 2 → Doctor, Patient, Room, Schedule
Bed 4 2 → Patient
BillingAccount 5 3 → Patient
CareTask 5 2 → Nurse, Patient
ConsultationNote 5 2 → Doctor, Patient
Department 5 2 → StaffMember, Ward
Diagnosis 5 2 → Doctor
DischargeSummary 5 2 → Doctor, Patient, Schedule
Doctor 4 2 → Patient, StaffMember
Equipment 5 2 → Department
FollowUp 5 2 → Doctor, Patient, Schedule
Hospital 5 2 → Appointment, Department, Ward
ImagingResult 5 2 → Doctor, Patient
InsuranceClaim 5 2 → InsurancePolicy
InsurancePolicy 4 2 →
LabResult 6 2 → Patient
MealPlan 5 2 → Patient
MedicalHistory 5 2 → Patient
MedicalRecord 4 2 → Diagnosis, Patient, Visit
Medication 4 2 →
MedicationOrder 4 2 → Medication
Nurse 4 2 → Patient, StaffMember
Patient 7 2 → Allergy, Doctor, Prescription
PatientPortalAccount 4 2 → Patient
Pharmacist 3 2 → Medication, MedicationOrder, StaffMember
Prescription 5 2 → Doctor, MedicationOrder, Patient
Procedure 4 2 →
Receptionist 3 2 → Appointment, StaffMember
RehabilitationPlan 5 2 → Patient, Therapist
Room 4 2 → Bed, Patient
SanitationChecklist 4 3 → Ward
Schedule 4 2 →
SecurityIncident 6 2 → StaffMember
Shift 4 2 → Schedule, StaffMember
StaffMember 5 2 → Department, Shift
SupplyOrder 5 2 → Department
SupportTicket 6 2 →
Surgeon 3 2 → Room, StaffMember, SurgerySchedule
Technician 4 2 → Equipment, StaffMember
Therapist 4 2 → StaffMember, TherapySession
TherapySession 5 2 → Patient, Schedule, Therapist
TreatmentPlan 5 2 → Doctor, Patient, Procedure, TherapySession
Visit 5 2 → Doctor, Patient
VitalSigns 4 2 →
Volunteer 5 2 → Department
Ward 4 2 → Bed, Nurse, Room

Exceptions (12):
----------------

AppointmentConflictException 0 1 →
BedUnavailableException 0 1 →
BillingOverdueException 0 1 →
EquipmentMaintenanceException 0 1 →
InfectionControlBreachException 0 1 →
InsuranceClaimDeniedException 0 1 →
LabResultDelayException 0 1 →
MedicationOutOfStockException 0 1 →
PatientNotFoundException 0 1 →
SurgeryScheduleException 0 1 →
TrainingRequirementException 0 1 →
UnauthorizedAccessException 0 1 →

Итоги
-----

Поля: 230
Поведения: 114
Ассоциации: 87
Исключения: 12

