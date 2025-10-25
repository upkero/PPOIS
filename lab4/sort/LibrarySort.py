from __future__ import annotations

from bisect import bisect_left, insort
from typing import Callable, Iterable, List, Optional, Sequence, TypeVar

T = TypeVar("T")
K = TypeVar("K")


class LibrarySort:
    """Implementation of Library Sort capable of handling arbitrary comparable objects.

    The algorithm maintains a sparse "shelf" with gaps between elements to allow relatively
    cheap insertions. When the shelf runs out of gaps, the structure is rebalanced by
    spreading the elements across a larger shelf.
    """

    @staticmethod
    def sort(
        iterable: Iterable[T],
        key: Optional[Callable[[T], K]] = None,
        *,
        initial_growth_factor: int = 4,
    ) -> List[T]:
        """Return a sorted list built using the Library Sort algorithm.

        Args:
            iterable: Source iterable to sort.
            key: Optional key extractor, mirroring the built-in `sorted`.
            initial_growth_factor: Multiplier that controls how much slack space the
                initial shelf receives. Increasing the factor reduces the number of
                required rebalances at the cost of additional memory.

        Returns:
            A list containing the sorted elements from `iterable`.
        """

        items = list(iterable)
        if len(items) <= 1:
            return items.copy()

        key_fn: Callable[[T], K] = key or (lambda value: value)  # type: ignore[misc]

        shelf_capacity = max(len(items) * initial_growth_factor, len(items) * 3 + 1)
        shelf: List[Optional[T]] = [None] * shelf_capacity
        occupied: List[int] = []

        # Place the first element roughly in the middle of the shelf.
        first_index = shelf_capacity // 2
        shelf[first_index] = items[0]
        occupied.append(first_index)

        for item in items[1:]:
            inserted = LibrarySort._insert(shelf, occupied, item, key_fn)
            if not inserted:
                shelf, occupied = LibrarySort._rebalance(shelf, occupied)
                # A second attempt must succeed because the shelf now has fresh gaps.
                if not LibrarySort._insert(shelf, occupied, item, key_fn):
                    raise RuntimeError("LibrarySort: rebalance failed to create a gap.")

        return [element for element in shelf if element is not None]

    @staticmethod
    def _insert(
        shelf: List[Optional[T]],
        occupied: List[int],
        item: T,
        key_fn: Callable[[T], K],
    ) -> bool:
        if not occupied:
            index = len(shelf) // 2
            shelf[index] = item
            occupied.append(index)
            return True

        left, right = LibrarySort._find_neighbour_indices(shelf, occupied, item, key_fn)
        gap_index = LibrarySort._find_gap_index(shelf, left, right)
        if gap_index is None:
            return False

        shelf[gap_index] = item
        insort(occupied, gap_index)
        return True

    @staticmethod
    def _find_neighbour_indices(
        shelf: Sequence[Optional[T]],
        occupied: Sequence[int],
        item: T,
        key_fn: Callable[[T], K],
    ) -> tuple[Optional[int], Optional[int]]:
        values = [shelf[idx] for idx in occupied]
        keys = [key_fn(value) for value in values]  # type: ignore[arg-type]
        target_key = key_fn(item)
        position = bisect_left(keys, target_key)

        left = occupied[position - 1] if position > 0 else None
        right = occupied[position] if position < len(occupied) else None
        return left, right

    @staticmethod
    def _find_gap_index(
        shelf: Sequence[Optional[T]],
        left: Optional[int],
        right: Optional[int],
    ) -> Optional[int]:
        if left is None and right is None:
            return len(shelf) // 2

        if left is None:
            start = right - 1 if right is not None else len(shelf) - 1
            for idx in range(start, -1, -1):
                if shelf[idx] is None:
                    return idx
            return None

        if right is None:
            for idx in range(left + 1, len(shelf)):
                if shelf[idx] is None:
                    return idx
            return None

        for idx in range(right - 1, left, -1):
            if shelf[idx] is None:
                return idx
        return None

    @staticmethod
    def _rebalance(
        shelf: Sequence[Optional[T]],
        occupied: Sequence[int],
    ) -> tuple[List[Optional[T]], List[int]]:
        elements = [shelf[index] for index in occupied]
        compact_elements = [element for element in elements if element is not None]
        count = len(compact_elements)
        if count == 0:
            return [None] * 1, []

        new_capacity = max(len(shelf) * 2, count * 3 + 1)
        new_shelf: List[Optional[T]] = [None] * new_capacity
        new_occupied: List[int] = []

        divider = count + 1
        for idx, element in enumerate(compact_elements, start=1):
            position = max((idx * new_capacity) // divider - 1, 0)
            while position < new_capacity and new_shelf[position] is not None:
                position += 1
            if position >= new_capacity:
                position = new_capacity - 1
                while new_shelf[position] is not None and position >= 0:
                    position -= 1
            if position < 0:
                raise RuntimeError("LibrarySort: unable to spread elements during rebalance.")
            new_shelf[position] = element
            new_occupied.append(position)

        return new_shelf, new_occupied

