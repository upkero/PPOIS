from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Reward:
    reward_id: str
    description: str
    required_points: int

    def is_affordable(self, points: int) -> bool:
        return points >= self.required_points

    def formatted(self) -> str:
        return f"{self.description} ({self.required_points} pts)"
