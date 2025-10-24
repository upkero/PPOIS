from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SafetyInspection:
    inspection_id: str
    inspector: str
    findings: list[str] = field(default_factory=list)
    status: str = "open"

    def add_finding(self, finding: str) -> None:
        self.findings.append(finding)

    def close(self) -> None:
        self.status = "closed"
