from __future__ import annotations

import unittest
from typing import List, Optional

from Book import Book
from LibrarySort import LibrarySort


class LibrarySortTests(unittest.TestCase):
    def test_sort_basic_integers(self) -> None:
        values = [5, 1, 9, -2, 0, 5]
        self.assertEqual(LibrarySort.sort(values), sorted(values))

    def test_sort_custom_objects_with_key(self) -> None:
        books = [
            Book(title="A", author="Auth", year=2010, rating=4.2),
            Book(title="B", author="Auth", year=2005, rating=4.7),
            Book(title="C", author="Auth", year=2005, rating=4.3),
        ]

        sorted_books = LibrarySort.sort(books, key=lambda book: (book.year, -book.rating))
        expected = [
            books[1],  # 2005, rating 4.7
            books[2],  # 2005, rating 4.3
            books[0],  # 2010
        ]
        self.assertEqual(sorted_books, expected)

    def test_insert_into_empty_shelf_places_element_in_middle(self) -> None:
        shelf: List[Optional[int]] = [None] * 5
        occupied: List[int] = []
        inserted = LibrarySort._insert(shelf, occupied, 10, lambda x: x)  # type: ignore[arg-type]

        self.assertTrue(inserted)
        self.assertEqual(len(occupied), 1)
        self.assertEqual(occupied[0], len(shelf) // 2)
        self.assertEqual(shelf[occupied[0]], 10)

    def test_find_gap_index_variants(self) -> None:
        shelf: List[Optional[int]] = [None, None, None]
        # Both neighbours absent
        self.assertEqual(LibrarySort._find_gap_index(shelf, None, None), 1)

        shelf_with_right: List[Optional[int]] = [None, 7, None, None]
        self.assertEqual(LibrarySort._find_gap_index(shelf_with_right, None, 1), 0)

        shelf_with_left: List[Optional[int]] = [None, 4, None, None]
        self.assertEqual(LibrarySort._find_gap_index(shelf_with_left, 1, None), 2)

        contiguous: List[Optional[int]] = [1, 2, 3]
        self.assertIsNone(LibrarySort._find_gap_index(contiguous, 0, 2))

    def test_rebalance_spreads_elements(self) -> None:
        shelf: List[Optional[int]] = [None] * 10
        occupied_indices = [1, 2, 3, 4]
        for index, value in zip(occupied_indices, [10, 20, 30, 40]):
            shelf[index] = value

        new_shelf, new_occupied = LibrarySort._rebalance(shelf, occupied_indices)
        self.assertEqual(len(new_occupied), len(occupied_indices))
        self.assertTrue(all(new_shelf[index] is not None for index in new_occupied))
        # Ensure elements are still present after rebalance
        rebalanced_values = [new_shelf[index] for index in new_occupied]
        self.assertCountEqual(rebalanced_values, [10, 20, 30, 40])


if __name__ == "__main__":
    unittest.main()
