from __future__ import annotations

from datetime import datetime, timedelta

from hospital.core.Appointment import Appointment
from hospital.core.Department import Department
from hospital.core.Diagnosis import Diagnosis
from hospital.core.Hospital import Hospital
from hospital.core.MedicalRecord import MedicalRecord
from hospital.core.Room import Room
from hospital.core.Schedule import Schedule
from hospital.core.Shift import Shift
from hospital.core.Visit import Visit
from hospital.core.Ward import Ward
from hospital.patients.Allergy import Allergy
from hospital.patients.BillingAccount import BillingAccount
from hospital.patients.InsurancePolicy import InsurancePolicy
from hospital.patients.LabResult import LabResult
from hospital.patients.MedicalHistory import MedicalHistory
from hospital.patients.MedicationOrder import MedicationOrder
from hospital.patients.Patient import Patient
from hospital.patients.PatientPortalAccount import PatientPortalAccount
from hospital.patients.Prescription import Prescription
from hospital.resources.Ambulance import Ambulance
from hospital.resources.Bed import Bed
from hospital.resources.Equipment import Equipment
from hospital.resources.MealPlan import MealPlan
from hospital.resources.SanitationChecklist import SanitationChecklist
from hospital.resources.SupplyOrder import SupplyOrder
from hospital.staff.Administrator import Administrator
from hospital.staff.Doctor import Doctor
from hospital.staff.Nurse import Nurse
from hospital.staff.Pharmacist import Pharmacist
from hospital.staff.Receptionist import Receptionist
from hospital.staff.StaffMember import StaffMember
from hospital.staff.Surgeon import Surgeon
from hospital.staff.Therapist import Therapist
from hospital.staff.Volunteer import Volunteer
from hospital.support.InsuranceClaim import InsuranceClaim
from hospital.support.SupportTicket import SupportTicket
from hospital.treatment.CareTask import CareTask
from hospital.treatment.ConsultationNote import ConsultationNote
from hospital.treatment.DischargeSummary import DischargeSummary
from hospital.treatment.FollowUp import FollowUp
from hospital.treatment.Medication import Medication
from hospital.treatment.Procedure import Procedure
from hospital.treatment.RehabilitationPlan import RehabilitationPlan
from hospital.treatment.SurgerySchedule import SurgerySchedule
from hospital.treatment.TherapySession import TherapySession
from hospital.treatment.TreatmentPlan import TreatmentPlan
from hospital.security.SecurityIncident import SecurityIncident


def run_demo() -> None:
    hospital = Hospital(name="CityCare Medical Center", address="123 Health Ave")

    cardiology_department = Department(name="Cardiology", floor=5)
    orthopedics_department = Department(name="Orthopedics", floor=4)
    hospital.register_department(cardiology_department)
    hospital.register_department(orthopedics_department)

    ward_c1 = Ward(code="C1", specialty="Cardiac Recovery")
    ward_c1.rooms.append(
        Room(
            number="C105",
            level=5,
            beds=[Bed(bed_id="C105-A", ward_code="C1"), Bed(bed_id="C105-B", ward_code="C1")],
        )
    )
    cardiology_department.wards.append(ward_c1)
    hospital.wards.append(ward_c1)

    doctor_staff = StaffMember(staff_id="STF-001", name="Dr. Alice Novak", role="Cardiologist")
    nurse_staff = StaffMember(staff_id="STF-010", name="Nurse Ben Turner", role="Registered Nurse")
    surgeon_staff = StaffMember(staff_id="STF-004", name="Dr. Christine Lang", role="Cardiac Surgeon")
    therapist_staff = StaffMember(staff_id="STF-020", name="Liam Carter", role="Physiotherapist")
    pharmacist_staff = StaffMember(staff_id="STF-030", name="Irene Park", role="Pharmacist")
    receptionist_staff = StaffMember(staff_id="STF-040", name="Marco Diaz", role="Receptionist")
    admin_staff = StaffMember(staff_id="STF-050", name="Emma Watson", role="Administrator")
    volunteer = Volunteer(volunteer_id="VOL-100", name="Julia Kim")

    doctor = Doctor(staff_member=doctor_staff)
    nurse = Nurse(staff_member=nurse_staff)
    surgeon = Surgeon(staff_member=surgeon_staff)
    therapist = Therapist(staff_member=therapist_staff, focus_area="Cardiac Rehab")
    pharmacist = Pharmacist(staff_member=pharmacist_staff)
    receptionist = Receptionist(staff_member=receptionist_staff)
    administrator = Administrator(staff_member=admin_staff)

    doctor.add_specialty("Interventional Cardiology")
    cardiology_department.assign_head(doctor_staff)
    cardiology_department.add_staff_member(doctor_staff)
    cardiology_department.add_staff_member(nurse_staff)
    cardiology_department.add_staff_member(therapist_staff)
    cardiology_department.add_staff_member(pharmacist_staff)
    administrator.assign_department(cardiology_department)
    administrator.completed_trainings.append("HIPAA-2025")
    administrator.verify_training("HIPAA-2025")
    volunteer.assign_department(cardiology_department)
    volunteer.log_hours(5.0)

    day_start = datetime(2025, 7, 14, 8, 0)
    doctor_shift = Shift(code="DAYCARD", schedule=Schedule(start=day_start, end=day_start + timedelta(hours=10), location="Cardiology"))
    doctor_shift.assign_staff(doctor_staff)
    doctor_shift.set_supervisor(doctor_staff)
    doctor_staff.add_shift(doctor_shift)

    patient = Patient(patient_id="PAT-9001", name="Samuel Green", date_of_birth="1980-03-12", contact_number="+1-202-555-0199")
    patient.assign_doctor(doctor)
    patient.add_allergy(Allergy(allergen="Penicillin", reaction="Rash", severity="Severe"))
    doctor.assign_patient(patient)
    nurse.add_certification("ACLS")
    therapist.add_certification("Cardiac Rehab Specialist")
    ward_c1.rooms[0].admit_patient(patient)

    medical_history = MedicalHistory(history_id="HIST-9001", patient=patient)
    medical_history.add_condition("Hypertension")

    insurance_policy = InsurancePolicy(policy_number="INS-777", provider="HealthyLife", coverage_limit=50000.0, expiry_date="2026-12-31")
    billing_account = BillingAccount(account_id="BILL-9001", patient=patient, insurance_policy=insurance_policy)
    billing_account.add_charge(3200.0)
    billing_account.record_payment(1500.0)
    billing_account.record_payment(800.0)

    appointment_schedule = Schedule(start=day_start + timedelta(hours=1), end=day_start + timedelta(hours=2), location="Consult Room 2")
    appointment = Appointment(identifier="APP-5001", patient=patient, doctor=doctor, room=ward_c1.rooms[0], schedule=appointment_schedule)
    hospital.schedule_appointment(appointment)
    appointment.confirm()
    receptionist.register_appointment(appointment)

    visit = Visit(visit_id="VIS-6001", patient=patient, doctor=doctor, visit_time=appointment_schedule.start)
    visit.add_note("Initial cardiac evaluation completed.")

    medical_record = MedicalRecord(record_id="MR-5001", patient=patient)
    medical_record.log_visit(visit)
    diagnosis = Diagnosis(code="I20.0", description="Unstable Angina", diagnosed_by=doctor, severity="Severe")
    diagnosis.add_symptom("Chest pain")
    medical_record.add_diagnosis(diagnosis)

    medication = Medication(medication_id="MED-1001", name="Nitroglycerin", form="Tablet", stock_level=150)
    pharmacist.add_inventory_item(medication)
    medication_order = MedicationOrder(medication=medication, dosage="0.4 mg", frequency="Once daily", quantity=30)
    pharmacist.dispense_medication(medication_order)
    prescription = Prescription(prescription_id="PRX-7001", patient=patient, prescribed_by=doctor)
    prescription.add_medication(medication_order)
    patient.prescriptions.append(prescription)

    therapy_schedule = Schedule(start=day_start + timedelta(hours=3), end=day_start + timedelta(hours=4), location="Rehab Room")
    therapy_session = TherapySession(session_id="TH-2001", patient=patient, therapist=therapist, schedule=therapy_schedule, session_type="Physiotherapy")
    therapist.schedule_session(therapy_session)

    procedure = Procedure(code="PR-45", name="Angioplasty", duration_minutes=120, requires_anesthesia=True)
    treatment_plan = TreatmentPlan(plan_id="PLAN-8001", patient=patient, primary_doctor=doctor)
    treatment_plan.add_procedure(procedure)
    treatment_plan.attach_therapy(therapy_session)

    surgery_schedule = SurgerySchedule(
        surgery_id="SURG-1001",
        patient=patient,
        surgeon=surgeon,
        room=ward_c1.rooms[0],
        schedule=Schedule(start=day_start + timedelta(days=1), end=day_start + timedelta(days=1, hours=3), location="Operating Theatre 1"),
    )
    surgeon.add_surgery(surgery_schedule)
    surgery_schedule.ensure_room_prepared(is_ready=True)

    care_task = CareTask(task_id="TASK-55", description="Monitor post-op vitals", assigned_nurse=nurse, patient=patient)
    nurse.assign_patient_care(patient)
    care_task.mark_completed()

    discharge_summary = DischargeSummary(summary_id="DIS-9001", patient=patient, attending_doctor=doctor)
    discharge_summary.add_recommendation("Continue medication as prescribed.")
    follow_up_schedule = Schedule(start=day_start + timedelta(days=7), end=day_start + timedelta(days=7, hours=1), location="Cardiology Follow-up")
    discharge_summary.set_follow_up(follow_up_schedule)

    follow_up = FollowUp(follow_up_id="FU-123", patient=patient, scheduled_with=doctor, schedule=follow_up_schedule)
    follow_up.update_notes("Monitor blood pressure daily.")

    rehab_plan = RehabilitationPlan(plan_id="REHAB-321", patient=patient, therapist=therapist)
    rehab_plan.add_goal("Improve stamina to 30 minutes of walking.")
    rehab_plan.record_progress("Patient completed 15-minute walk.")

    consultation_note = ConsultationNote(
        note_id="NOTE-12",
        doctor=doctor,
        patient=patient,
        content="Discussed lifestyle changes and medication adherence.",
        created_on=appointment_schedule.start.strftime("%Y-%m-%d"),
    )
    consultation_note.append_content("Patient will attend weekly rehab sessions.")

    lab_result = LabResult(
        result_id="LAB-456",
        patient=patient,
        test_type="Blood Panel",
        collected_at=day_start + timedelta(hours=2),
    )
    lab_result.release(findings="Cholesterol slightly elevated.", release_time=day_start + timedelta(hours=6))
    lab_result.ensure_timely_release(deadline_hours=8)

    supply_order = SupplyOrder(order_id="ORD-789", department=cardiology_department)
    supply_order.add_item("Sterile gloves", 120.0)
    supply_order.add_item("Heart monitors", 4500.0)
    supply_order.mark_received()

    equipment = Equipment(equipment_id="EQ-999", name="ECG Machine", department=cardiology_department)
    equipment.add_maintenance_log("Calibrated on schedule.")

    ambulance = Ambulance(vehicle_id="AMB-12")
    ambulance.crew.extend([doctor_staff, nurse_staff])
    ambulance.dispatch(call_id="EM-911")
    ambulance.mark_available()

    meal_plan = MealPlan(plan_id="MEAL-202", patient=patient, caloric_target=2200)
    meal_plan.add_meal("Low-sodium breakfast")
    meal_plan.add_restriction("No caffeine")

    checklist = SanitationChecklist(checklist_id="SAN-101", ward=ward_c1)
    checklist.add_task("Disinfect surfaces")
    checklist.add_task("Replace linens")
    checklist.complete_task("Disinfect surfaces")
    checklist.complete_task("Replace linens")
    checklist.verify_completion()

    insurance_claim = InsuranceClaim(claim_id="CLM-555", policy=insurance_policy, amount=2800.0)
    insurance_claim.approve()

    support_ticket = SupportTicket(ticket_id="SUP-888", submitted_by=patient.name, category="Portal", description="Unable to view lab results.")
    support_ticket.add_update("Issue resolved by IT.")
    support_ticket.close()

    portal_account = PatientPortalAccount(username="sgreen", patient=patient, password_hash="hashed-secret")
    portal_account.link_record(medical_record.record_id)
    portal_account.verify_access("hashed-secret")

    security_incident = SecurityIncident(
        incident_id="SEC-100",
        reported_by=receptionist_staff,
        description="Unattended visitor in restricted area.",
        occurred_at=day_start + timedelta(hours=5),
    )
    security_incident.add_person("Visitor John Doe")
    security_incident.mark_resolved()

    administrator.compliance_tasks.append("Annual safety audit")
    volunteer.tasks_completed.append("Guided patients to rehab center")
    billing_balance = billing_account.verify_balance()
    insurance_remaining = insurance_policy.remaining_coverage(sum(billing_account.charges))

    print("=== Hospital Management Scenario ===")
    print(f"Hospital departments: {[dept.name for dept in hospital.departments]}")
    print(f"Patient: {patient.name}, Primary Doctor: {patient.primary_doctor.staff_member.name}")
    print(f"Diagnosis: {diagnosis.description}, Critical: {diagnosis.is_critical()}")
    print(f"Treatment plan procedures: {[proc.name for proc in treatment_plan.procedures]}")
    print(f"Therapy sessions scheduled: {[session.session_id for session in treatment_plan.therapy_sessions]}")
    print(f"Surgery status: {surgery_schedule.status}")
    print(f"Prescription meds: {[order.medication.name for order in prescription.medications]}")
    print(f"Meal plan restrictions: {meal_plan.restrictions}")
    print(f"Supply order total: {supply_order.total_cost}")
    print(f"Insurance claim status: {insurance_claim.status}")
    print(f"Support ticket status: {support_ticket.status}")
    print(f"Remaining billing balance: {billing_balance:.2f}")
    print(f"Insurance remaining coverage: {insurance_remaining:.2f}")
    print(f"Portal access linked records: {portal_account.linked_records}")
    print(f"Security incident resolved: {security_incident.resolved}")


if __name__ == "__main__":
    run_demo()
