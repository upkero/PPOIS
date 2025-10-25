from __future__ import annotations

from dataclasses import dataclass


@dataclass(order=True)
class Book:
    """Simple data class representing a book in a library catalogue."""

    year: int
    rating: float
    title: str
    author: str

    def __repr__(self) -> str:
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"year={self.year}, rating={self.rating:.1f})"
        )

