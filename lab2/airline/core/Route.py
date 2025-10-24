from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Route:
    origin: Airport
    destination: Airport
    distance_km: int
    waypoints: list[str] = field(default_factory=list)

    def estimate_duration_hours(self, average_speed_kmh: int) -> float:
        if average_speed_kmh <= 0:
            raise ValueError("Average speed must be positive.")
        return round(self.distance_km / average_speed_kmh, 2)

    def add_waypoint(self, waypoint: str) -> None:
        if waypoint not in self.waypoints:
            self.waypoints.append(waypoint)
