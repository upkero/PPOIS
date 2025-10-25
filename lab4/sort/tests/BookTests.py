from __future__ import annotations

import unittest

from Book import Book


class BookTests(unittest.TestCase):
    def test_ordering_uses_year_then_rating(self) -> None:
        old_book = Book(title="Old", author="Auth", year=1990, rating=4.8)
        new_book = Book(title="New", author="Auth", year=2000, rating=4.0)
        self.assertLess(old_book, new_book)

        better_rating = Book(title="Better", author="Auth", year=2000, rating=4.9)
        worse_rating = Book(title="Worse", author="Auth", year=2000, rating=4.2)
        self.assertLess(worse_rating, better_rating)

    def test_repr_contains_fields(self) -> None:
        book = Book(title="Title", author="Author", year=2020, rating=4.5)
        representation = repr(book)
        self.assertIn("Title", representation)
        self.assertIn("Author", representation)
        self.assertIn("2020", representation)
        self.assertIn("4.5", representation)


if __name__ == "__main__":
    unittest.main()

