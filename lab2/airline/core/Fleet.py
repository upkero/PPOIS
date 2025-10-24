from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Fleet:
    name: str
    manager: str
    aircraft: list[Aircraft] = field(default_factory=list)

    def add_aircraft(self, aircraft: Aircraft) -> None:
        if aircraft not in self.aircraft:
            self.aircraft.append(aircraft)

    def total_capacity(self) -> int:
        return sum(item.capacity for item in self.aircraft)
