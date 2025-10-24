from __future__ import annotations

from dataclasses import dataclass, field

from airline.exceptions.LoyaltyTierUpgradeException import LoyaltyTierUpgradeException


@dataclass
class LoyaltyMember:
    passenger: Passenger
    tier: str
    points: int
    rewards: list[Reward] = field(default_factory=list)

    def add_points(self, earned: int) -> None:
        if earned < 0:
            raise ValueError("Points cannot be negative.")
        self.points += earned

    def attempt_tier_upgrade(self, target_tier: str) -> None:
        tiers = ["Silver", "Gold", "Platinum"]
        if target_tier not in tiers:
            raise LoyaltyTierUpgradeException(f"Unknown tier {target_tier}.")
        current_index = tiers.index(self.tier)
        target_index = tiers.index(target_tier)
        if target_index <= current_index:
            raise LoyaltyTierUpgradeException("Upgrade target must be higher than current tier.")
        self.tier = target_tier
