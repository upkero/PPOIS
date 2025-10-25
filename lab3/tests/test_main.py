from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from main import run_demo


def test_run_demo_outputs(capsys):
    run_demo()
    output = capsys.readouterr().out.strip()
    expected = (
        "=== Hospital Management Scenario ===\n"
        "Hospital departments: ['Cardiology', 'Orthopedics']\n"
        "Patient: Samuel Green, Primary Doctor: Dr. Alice Novak\n"
        "Diagnosis: Unstable Angina, Critical: True\n"
        "Treatment plan procedures: ['Angioplasty']\n"
        "Therapy sessions scheduled: ['TH-2001']\n"
        "Surgery status: pending\n"
        "Prescription meds: ['Nitroglycerin']\n"
        "Meal plan restrictions: ['No caffeine']\n"
        "Supply order total: 4620.0\n"
        "Insurance claim status: approved\n"
        "Support ticket status: closed\n"
        "Remaining billing balance: 900.00\n"
        "Insurance remaining coverage: 46800.00\n"
        "Portal access linked records: ['MR-5001']\n"
        "Security incident resolved: True"
    )
    assert output == expected
