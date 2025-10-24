from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from hospital.exceptions.LabResultDelayException import LabResultDelayException


@dataclass
class LabResult:
    result_id: str
    patient: "Patient"
    test_type: str
    collected_at: datetime
    released_at: datetime | None = None
    findings: str = ""

    def release(self, findings: str, release_time: datetime) -> None:
        self.findings = findings
        self.released_at = release_time

    def ensure_timely_release(self, deadline_hours: int) -> None:
        if self.released_at is None:
            raise LabResultDelayException("Result has not been released yet.")
        elapsed = (self.released_at - self.collected_at).total_seconds() / 3600
        if elapsed > deadline_hours:
            raise LabResultDelayException("Result released after deadline.")
