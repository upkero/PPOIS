from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, List, TypeVar

T = TypeVar("T")


class BidirectionalIterator(Generic[T], Iterator[T]):
    """Generic bidirectional iterator with forward and backward traversal."""

    def __init__(self, items: Iterable[T], *, reverse: bool = False) -> None:
        self._items: List[T] = list(items)
        self._reverse = reverse
        self._index = len(self._items) - 1 if reverse else 0
        self._last_index: int | None = None

    def __iter__(self) -> BidirectionalIterator[T]:
        return self

    def __next__(self) -> T:
        if not self.is_valid():
            raise StopIteration
        value = self.current()
        self._last_index = self._index
        self._advance()
        return value

    def current(self) -> T:
        if not self.is_valid():
            raise StopIteration("Iterator is out of range")
        return self._items[self._index]

    def current_index(self) -> int:
        return self._index

    @property
    def reverse_flag(self) -> bool:
        return self._reverse

    def prev(self) -> T:
        if not self._items:
            raise StopIteration("Iterator contains no elements")

        next_index = self._index + 1 if self._reverse else self._index - 1
        if next_index < 0 or next_index >= len(self._items):
            raise StopIteration("Iterator is out of range")

        self._index = next_index
        self._last_index = self._index
        return self.current()

    def _advance(self) -> None:
        if self._reverse:
            self._index -= 1
        else:
            self._index += 1

    def is_valid(self) -> bool:
        return 0 <= self._index < len(self._items)

    def reset(self) -> None:
        self._index = len(self._items) - 1 if self._reverse else 0
        self._last_index = None

    def clone(self) -> BidirectionalIterator[T]:
        copy = BidirectionalIterator(self._items, reverse=self._reverse)
        copy._index = self._index
        copy._last_index = self._last_index
        return copy

    def reverse(self) -> BidirectionalIterator[T]:
        return BidirectionalIterator(
            reversed(self._items),
            reverse=not self._reverse,
        )

    def to_list(self) -> list[T]:
        return list(self._items)

    def set_index(self, index: int) -> None:
        self._index = index
        self._last_index = None

    def set_last_index(self, last_index: int | None) -> None:
        self._last_index = last_index

    def last_index(self) -> int | None:
        return self._last_index

    def last(self) -> T:
        if self._last_index is None:
            raise StopIteration("Iterator has not produced any elements yet")
        return self._items[self._last_index]
