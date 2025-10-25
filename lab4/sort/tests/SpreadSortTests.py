from __future__ import annotations

import math
import unittest

from SpreadSort import SpreadSort


class SpreadSortTests(unittest.TestCase):
    def test_sort_integers_matches_builtin(self) -> None:
        values = [42, -5, 0, 17, 17, 1024]
        self.assertEqual(SpreadSort.sort(values), sorted(values))

    def test_sort_floats(self) -> None:
        values = [math.pi, math.e, -1.5, 0.0, 2.0]
        result = SpreadSort.sort(values)
        self.assertEqual(result, sorted(values))

    def test_sort_custom_objects(self) -> None:
        class Score:
            def __init__(self, name: str, value: float) -> None:
                self.name = name
                self.value = value

            def __repr__(self) -> str:  # pragma: no cover - debug helper
                return f"Score({self.name!r}, {self.value})"

        scores = [Score("a", 10.5), Score("b", 5.1), Score("c", 8.8)]
        result = SpreadSort.sort(scores, key=lambda score: score.value)
        self.assertEqual([score.name for score in result], ["b", "c", "a"])

    def test_identical_keys_returns_copy(self) -> None:
        values = [1.0] * 10
        sorted_values = SpreadSort.sort(values)
        self.assertEqual(sorted_values, values)
        self.assertIsNot(sorted_values, values)

    def test_recursive_bucket_refinement(self) -> None:
        # Use a wide range to trigger multiple buckets and recursive refinement.
        values = list(range(200, -1, -1))
        result = SpreadSort.sort(values, bucket_size=10)
        self.assertEqual(result, sorted(values))


if __name__ == "__main__":
    unittest.main()

