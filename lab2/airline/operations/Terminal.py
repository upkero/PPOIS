from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Terminal:
    name: str
    airport: Airport
    gates: list[Gate] = field(default_factory=list)
    amenities: list[str] = field(default_factory=list)

    def add_gate(self, gate: Gate) -> None:
        self.gates.append(gate)

    def add_amenity(self, amenity: str) -> None:
        if amenity not in self.amenities:
            self.amenities.append(amenity)
