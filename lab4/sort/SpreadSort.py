from __future__ import annotations

from typing import Callable, Iterable, List, Optional, TypeVar

T = TypeVar("T")
K = TypeVar("K", int, float)


class SpreadSort:
    """Spreadsort implementation for numeric keys.

    Spreadsort is a hybrid of radix and comparison sorting. The implementation below
    partitions the data into buckets using the span between the minimum and maximum keys,
    recursively refining oversized buckets until they become small enough for a comparison
    sort. For small inputs a straightforward `sorted` call is used.
    """

    @staticmethod
    def sort(
        iterable: Iterable[T],
        key: Optional[Callable[[T], K]] = None,
        *,
        bucket_size: int = 32,
    ) -> List[T]:
        """Return a list sorted with the Spreadsort algorithm.

        Args:
            iterable: Source iterable to sort.
            key: Optional extractor that must return numeric values suitable for range
                calculations. Defaults to the identity function.
            bucket_size: Threshold at which the algorithm falls back to a comparison sort.

        Returns:
            Items from `iterable` sorted in ascending order.
        """

        items = list(iterable)
        if len(items) <= 1:
            return items.copy()

        key_fn: Callable[[T], K] = key or (lambda value: value)  # type: ignore[misc]
        return SpreadSort._spreadsort(items, key_fn, bucket_size)

    @staticmethod
    def _spreadsort(
        items: List[T],
        key_fn: Callable[[T], K],
        bucket_size: int,
    ) -> List[T]:
        if len(items) <= bucket_size:
            return sorted(items, key=key_fn)

        keys = [key_fn(item) for item in items]
        minimum = min(keys)
        maximum = max(keys)

        if minimum == maximum:
            return items.copy()

        spread = maximum - minimum
        bucket_count = max(2, int(len(items) ** 0.5))
        bucket_width = spread / bucket_count or 1

        buckets: List[List[T]] = [[] for _ in range(bucket_count)]
        for item, k in zip(items, keys):
            index = int((k - minimum) / bucket_width)
            if index >= bucket_count:
                index = bucket_count - 1
            buckets[index].append(item)

        result: List[T] = []
        for bucket in buckets:
            if not bucket:
                continue
            if len(bucket) > bucket_size and bucket_width > 0:
                result.extend(SpreadSort._spreadsort(bucket, key_fn, bucket_size))
            else:
                result.extend(sorted(bucket, key=key_fn))
        return result

