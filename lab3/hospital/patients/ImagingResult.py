from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ImagingResult:
    image_id: str
    patient: "Patient"
    modality: str
    radiologist: "Doctor"
    interpretation: str = ""

    def add_interpretation(self, text: str) -> None:
        self.interpretation = text

    def summary(self) -> str:
        return f"{self.modality} result for {self.patient.name}"
