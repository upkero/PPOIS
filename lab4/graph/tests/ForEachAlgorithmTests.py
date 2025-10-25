from __future__ import annotations

import unittest

from ForEachAlgorithm import ForEachAlgorithm


class ForEachAlgorithmTests(unittest.TestCase):
    def test_apply_runs_callable_for_all_items(self) -> None:
        items = [1, 2, 3]
        collected: list[int] = []

        def capture(value: int) -> None:
            collected.append(value * 2)

        ForEachAlgorithm.apply(items, capture)
        self.assertEqual(collected, [2, 4, 6])


if __name__ == "__main__":
    unittest.main()
