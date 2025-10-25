from __future__ import annotations

import unittest

from BidirectionalIterator import BidirectionalIterator


class BidirectionalIteratorTests(unittest.TestCase):
    def test_forward_iteration_and_last(self) -> None:
        iterator = BidirectionalIterator([1, 2, 3])
        values = list(iterator)
        self.assertEqual(values, [1, 2, 3])
        self.assertEqual(iterator.last(), 3)

    def test_prev_navigation(self) -> None:
        iterator = BidirectionalIterator([1, 2, 3])
        first = next(iterator)
        self.assertEqual(first, 1)
        second = next(iterator)
        self.assertEqual(second, 2)
        self.assertEqual(iterator.prev(), 2)
        self.assertEqual(iterator.prev(), 1)
        with self.assertRaises(StopIteration):
            iterator.prev()

    def test_reverse_and_clone(self) -> None:
        iterator = BidirectionalIterator([1, 2, 3], reverse=True)
        clone = iterator.clone()
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(clone), 3)
        self.assertEqual(next(iterator), 2)
        reverse = iterator.reverse()
        self.assertEqual(reverse.to_list(), [3, 2, 1])

    def test_reset_and_last_without_iteration(self) -> None:
        iterator = BidirectionalIterator([1])
        iterator.reset()
        with self.assertRaises(StopIteration):
            iterator.last()


if __name__ == "__main__":
    unittest.main()
