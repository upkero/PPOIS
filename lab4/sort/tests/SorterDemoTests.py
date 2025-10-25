from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from SorterDemo import SorterDemo


class SorterDemoTests(unittest.TestCase):
    def test_run_produces_expected_sections(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            SorterDemo.run()

        output = buffer.getvalue()
        self.assertIn("LibrarySort on integers", output)
        self.assertIn("SpreadSort on floats", output)
        self.assertIn("LibrarySort on custom Book objects", output)
        self.assertIn("SpreadSort on the same books", output)


if __name__ == "__main__":
    unittest.main()

