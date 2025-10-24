from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Airport:
    name: str
    city: str
    gates: list[Gate] = field(default_factory=list)
    terminals: list[Terminal] = field(default_factory=list)
    runways: list[Runway] = field(default_factory=list)

    def add_terminal(self, terminal: Terminal) -> None:
        if terminal not in self.terminals:
            self.terminals.append(terminal)

    def assign_gate_to_flight(self, gate_number: str, flight: Flight) -> bool:
        for gate in self.gates:
            if gate.gate_number == gate_number:
                gate.assign_flight(flight)
                return True
        return False
