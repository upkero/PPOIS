from __future__ import annotations

from LibrarySort import LibrarySort
from SpreadSort import SpreadSort
from Book import Book


class SorterDemo:
    """Showcase for LibrarySort and SpreadSort on built-in and custom objects."""

    @staticmethod
    def run() -> None:
        SorterDemo._demo_integers()
        SorterDemo._demo_floats()
        SorterDemo._demo_books()

    @staticmethod
    def _demo_integers() -> None:
        values = [42, 7, 1024, -3, 7, 19, 0, 5]
        print("LibrarySort on integers:")
        print("  input :", values)
        print("  output:", LibrarySort.sort(values))
        print()

    @staticmethod
    def _demo_floats() -> None:
        values = [3.14, 2.71, -1.0, 0.0, 10.5, 2.0]
        print("SpreadSort on floats:")
        print("  input :", values)
        print("  output:", SpreadSort.sort(values))
        print()

    @staticmethod
    def _demo_books() -> None:
        books = [
            Book(title="The Pragmatic Programmer", author="Hunt & Thomas", year=1999, rating=4.8),
            Book(title="Clean Code", author="Robert C. Martin", year=2008, rating=4.7),
            Book(title="Design Patterns", author="Gamma et al.", year=1994, rating=4.5),
            Book(title="Refactoring", author="Martin Fowler", year=1999, rating=4.6),
            Book(title="Introduction to Algorithms", author="Cormen et al.", year=2009, rating=4.3),
        ]

        print("LibrarySort on custom Book objects (sorted by year, then rating):")
        sorted_by_year = LibrarySort.sort(books, key=lambda book: (book.year, -book.rating))
        for book in sorted_by_year:
            print(f"  {book}")

        print("\nSpreadSort on the same books (sorted by rating descending):")
        sorted_by_rating = SpreadSort.sort(books, key=lambda book: -book.rating)
        for book in sorted_by_rating:
            print(f"  {book}")
        print()

