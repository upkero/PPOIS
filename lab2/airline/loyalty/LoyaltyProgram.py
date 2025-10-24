from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LoyaltyProgram:
    name: str
    tiers: list[str] = field(default_factory=lambda: ["Silver", "Gold", "Platinum"])
    members: list[LoyaltyMember] = field(default_factory=list)

    def register_member(self, member: LoyaltyMember) -> None:
        if member not in self.members:
            self.members.append(member)

    def find_tier(self, points: int) -> str:
        if points >= 70000:
            return "Platinum"
        if points >= 30000:
            return "Gold"
        return "Silver"
