from __future__ import annotations

from collections.abc import Iterable, Callable
from typing import TypeVar

T = TypeVar("T")


class ForEachAlgorithm:
    """Utility that mimics std::for_each for educational purposes."""

    @staticmethod
    def apply(items: Iterable[T], function: Callable[[T], None]) -> None:
        for item in items:
            function(item)
