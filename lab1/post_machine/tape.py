from dataclasses import dataclass, field
from typing import Dict, Iterable, Optional


@dataclass(slots=True)
class Tape:
    """
    Bi-infinite tape on integers, sparse storage.
    Unset cells read as DEFAULT_BLANK ('_').
    """
    
    DEFAULT_BLANK = "_"
    _cells: Dict[int, str] = field(default_factory=dict)
    _visited_min: Optional[int] = None
    _visited_max: Optional[int] = None

    def read(self, pos: int) -> str:
        v = self._cells.get(pos, self.DEFAULT_BLANK)
        self._mark_visit(pos)
        return v

    def write(self, pos: int, sym: str) -> None:
        if not isinstance(sym, str) or len(sym) != 1:
            raise ValueError("Symbol must be one-character string")
        if sym == self.DEFAULT_BLANK:
            self._cells.pop(pos, None)
        else:
            self._cells[pos] = sym
        self._mark_visit(pos)

    def bulk_load(self, s: str, head: int = 0, blank: str = DEFAULT_BLANK) -> None:
        """
        Load contiguous symbols so that s[0] at position 0.
        Head is not stored here (Machine tracks head).
        """
        if not isinstance(s, str):
            raise TypeError("bulk_load expects a string")
        self._cells.clear()
        self._visited_min = self._visited_max = None
        for i, ch in enumerate(s):
            if ch != blank:
                self._cells[i] = ch

    def to_string(self, left: int, right: int, blank: str = DEFAULT_BLANK) -> str:
        """Return a window [left..right] inclusive as a string."""
        out = []
        for i in range(left, right + 1):
            out.append(self._cells.get(i, blank))
        return "".join(out)

    def minmax(self) -> tuple[int, int]:
        """Visited min/max (falls back to 0..0)."""
        if self._visited_min is None or self._visited_max is None:
            return (0, 0)
        return (self._visited_min, self._visited_max)

    def items(self) -> Iterable[tuple[int, str]]:
        return self._cells.items()

    # -------- internals --------
    def _mark_visit(self, pos: int) -> None:
        if self._visited_min is None:
            self._visited_min = self._visited_max = pos
        else:
            if pos < self._visited_min:
                self._visited_min = pos
            if pos > self._visited_max:
                self._visited_max = pos
