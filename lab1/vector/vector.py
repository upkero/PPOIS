from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering
import math
from typing import Tuple


@total_ordering
@dataclass(frozen=True, slots=True)
class Vector:
    """
    Immutable 3D vector.

    Features:
      - +, -, * (dot or scalar), / scalar, comparisons by length
      - cross(other)  -> Vector
      - length(), normalized(), cos(other)
      - from_points(), from_str()
    """
    x: float
    y: float
    z: float
    _EPS = 1e-9

    # ---------- factories ----------
    @classmethod
    def from_points(cls, p1: Tuple[float, float, float], p2: Tuple[float, float, float]) -> "Vector":
        """Create vector as p1->p2."""
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return cls(x2 - x1, y2 - y1, z2 - z1)

    @classmethod
    def from_str(cls, text: str) -> "Vector":
        """
        Parse "x y z" or "x,y,z" (spaces optional).
        Examples: "1 2 3", "1,2,3", "1, 2, 3"
        """
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        s = text.replace(",", " ").split()
        if len(s) != 3:
            raise ValueError(f"cannot parse Vector from: {text!r}")
        try:
            x, y, z = map(float, s)
        except ValueError as e:
            raise ValueError(f"cannot parse floats from: {text!r}") from e
        return cls(x, y, z)

    # ---------- basic ops ----------
    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __iadd__(self, other: "Vector") -> "Vector":
        # immutable -> return new
        return self.__add__(other)

    def __isub__(self, other: "Vector") -> "Vector":
        return self.__sub__(other)

    def __mul__(self, other) -> float | "Vector":
        """
        v * v -> dot product (float)
        v * s -> scalar multiply (Vector)
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if self._is_num(other):
            return Vector(self.x * float(other), self.y * float(other), self.z * float(other))
        return NotImplemented

    def __rmul__(self, other) -> "Vector":
        if self._is_num(other):
            return self * other
        return NotImplemented

    def __truediv__(self, other: float) -> "Vector":
        if not self._is_num(other):
            return NotImplemented
        denom = float(other)
        if abs(denom) < self._EPS:
            raise ZeroDivisionError("division by zero")
        return Vector(self.x / denom, self.y / denom, self.z / denom)

    def __itruediv__(self, other: float) -> "Vector":
        return self.__truediv__(other)

    # ---------- vector math ----------
    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self) -> "Vector":
        L = self.length()
        if L < self._EPS:
            raise ValueError("cannot normalize zero vector")
        return self / L

    def cross(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("cross() expects Vector")
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def cos(self, other: "Vector") -> float:
        """Cosine of angle between self and other."""
        if not isinstance(other, Vector):
            raise TypeError("cos() expects Vector")
        a = self.length()
        b = other.length()
        if a < self._EPS or b < self._EPS:
            raise ValueError("cos undefined for zero-length vector(s)")
        return (self * other) / (a * b)

    # ---------- comparisons ----------
    def _length_key(self) -> float:
        return self.length()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return (
            math.isclose(self.x, other.x, rel_tol=1e-9, abs_tol=1e-12)
            and math.isclose(self.y, other.y, rel_tol=1e-9, abs_tol=1e-12)
            and math.isclose(self.z, other.z, rel_tol=1e-9, abs_tol=1e-12)
        )

    def __lt__(self, other: "Vector") -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self._length_key() < other._length_key() - 1e-12

    # ---------- repr ----------
    def __repr__(self) -> str:
        return f"Vector(x={self.x:.12g}, y={self.y:.12g}, z={self.z:.12g})"

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z}"
    
    @staticmethod
    def _is_num(x) -> bool:
        return isinstance(x, (int, float))
