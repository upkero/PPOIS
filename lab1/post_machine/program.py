from typing import Dict, List, Optional

from .Instruction import Instruction
from .exeptions import ProgramParseError
from .ProgramMeta import ProgramMeta


class Program:
    """
    Program with labeled blocks:
      [label]
      INSTR
      INSTR
    """
    def __init__(self) -> None:
        self._blocks: Dict[str, List[Instruction]] = {}
        self._meta = ProgramMeta()

    @property
    def meta(self) -> ProgramMeta:
        return self._meta

    def labels(self) -> List[str]:
        return list(self._blocks.keys())

    def get_block(self, label: str) -> List[Instruction]:
        if label not in self._blocks:
            raise KeyError(f"no such label: {label}")
        return self._blocks[label]

    @staticmethod
    def _strip_comment(line: str) -> str:
        i = line.find("#")
        return line if i < 0 else line[:i]

    @classmethod
    def from_file(cls, path: str) -> "Program":
        p = cls()
        current_label: Optional[str] = None
        blocks: Dict[str, List[Instruction]] = {}
        start: Optional[str] = None
        head: Optional[int] = None
        tape_inline: Optional[str] = None

        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                line = cls._strip_comment(raw).strip()
                if not line:
                    continue

                # meta lines
                up = line.upper()
                if up.startswith("START:"):
                    start = line.split(":", 1)[1].strip() or None
                    continue
                if up.startswith("HEAD:"):
                    arg = line.split(":", 1)[1].strip()
                    if arg:
                        try:
                            head = int(arg)
                        except ValueError:
                            raise ProgramParseError(f"HEAD must be int: {arg!r}")
                    continue
                if up.startswith("TAPE:"):
                    tape_inline = line.split(":", 1)[1].strip() or ""
                    continue

                # block start?
                if line.startswith("[") and line.endswith("]") and len(line) >= 3:
                    label = line[1:-1].strip()
                    if not label:
                        raise ProgramParseError("empty label []")
                    if label in blocks:
                        raise ProgramParseError(f"duplicate label: {label}")
                    blocks[label] = []
                    current_label = label
                    continue

                # instruction
                if current_label is None:
                    raise ProgramParseError("instruction outside of any [label] block")
                try:
                    instr = Instruction.parse(line)
                except ValueError as e:
                    raise ProgramParseError(str(e))
                blocks[current_label].append(instr)

        if not blocks:
            raise ProgramParseError("no labeled blocks found")

        p._blocks = blocks
        p._meta = ProgramMeta(start_label=start, head=head, tape_inline=tape_inline)
        return p
