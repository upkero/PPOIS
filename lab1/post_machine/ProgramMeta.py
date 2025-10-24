from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, slots=True)
class ProgramMeta:
    start_label: Optional[str] = None
    head: Optional[int] = None
    tape_inline: Optional[str] = None