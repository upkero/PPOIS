from dataclasses import dataclass
from typing import Optional
from .Op import Op


@dataclass(frozen=True, slots=True)
class Instruction:
    op: Op
    arg: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.op.name}" + (f" {self.arg}" if self.arg is not None else "")

    @staticmethod
    def parse(line: str) -> "Instruction":
        """
        Parse a single instruction line (already stripped of comments).
        Supported:
          MARK | ERASE | R | L | HALT
          JZ <label> | JNZ <label> | GOTO <label>
        """
        if not isinstance(line, str):
            raise TypeError("line must be string")
        s = line.strip()
        if not s:
            raise ValueError("empty instruction")

        parts = s.split()
        op = parts[0].upper()
        arg = None
        if op in {"JZ", "JNZ", "GOTO"}:
            if len(parts) != 2:
                raise ValueError(f"{op} requires label arg")
            arg = parts[1]
        else:
            if len(parts) != 1:
                raise ValueError(f"{op} must have no arguments")

        try:
            if op == "MARK":
                return Instruction(Op.MARK)
            if op == "ERASE":
                return Instruction(Op.ERASE)
            if op == "R":
                return Instruction(Op.R)
            if op == "L":
                return Instruction(Op.L)
            if op == "JZ":
                return Instruction(Op.JZ, arg)
            if op == "JNZ":
                return Instruction(Op.JNZ, arg)
            if op == "GOTO":
                return Instruction(Op.GOTO, arg)
            if op == "HALT":
                return Instruction(Op.HALT)
        except Exception as e:  # pragma: no cover (safety net)
            raise ValueError(f"bad instruction: {line!r}") from e

        raise ValueError(f"unknown opcode: {op}")
