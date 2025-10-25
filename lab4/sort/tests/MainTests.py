from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from Main import Main


class MainTests(unittest.TestCase):
    def test_main_invokes_demo(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            Main.main()
        output = buffer.getvalue()
        self.assertIn("LibrarySort on integers", output)


if __name__ == "__main__":
    unittest.main()

