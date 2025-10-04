from dataclasses import dataclass
from typing import Callable, Optional, Tuple

from .Tape import Tape
from .Program import Program
from .Instruction import Instruction
from .Op import Op
from .exeptions import MachineHalt


@dataclass(slots=True)
class PostMachine:
    program: Program
    tape: Tape
    head: int = 0
    pc: Tuple[str, int] = ("", 0)  # (label, index)
    steps: int = 0

    def reset(
        self,
        *,
        tape: Optional[Tape] = None,
        head: Optional[int] = None,
        start_label: Optional[str] = None,
    ) -> None:
        if tape is not None:
            self.tape = tape
        if head is not None:
            self.head = head
        label = start_label or self.pc[0] or self._default_start()
        self.pc = (label, 0)
        self.steps = 0

    def _default_start(self) -> str:
        meta = self.program.meta
        if meta.start_label and meta.start_label in self.program.labels():
            return meta.start_label
        # pick the first declared label if none set
        return self.program.labels()[0]

    # ---------- execution ----------
    def step(self, *, on_halt_raise: bool = False) -> bool:
        label, idx = self.pc
        block = self.program.get_block(label)
        if idx >= len(block):
            # end of block without HALT: treat as HALT
            if on_halt_raise:
                raise MachineHalt("implicit HALT (end of block)")
            return False

        instr: Instruction = block[idx]
        self._exec(instr)
        self.steps += 1
        return instr.op is not Op.HALT

    def run(
        self,
        max_steps: Optional[int] = None,
        logger: Optional[Callable[[dict], None]] = None,
        on_halt_raise: bool = False,
    ) -> None:
        n = 0
        while True:
            alive = self.step(on_halt_raise=on_halt_raise)
            if logger:
                logger(self.state())
            if not alive:
                break
            n += 1
            if max_steps is not None and n >= max_steps:
                break

    def state(self) -> dict:
        lmin, lmax = self.tape.minmax()
        left = min(lmin, self.head - 16)
        right = max(lmax, self.head + 16)
        return {
            "pc": {"label": self.pc[0], "index": self.pc[1]},
            "head": self.head,
            "cell": self.tape.read(self.head),
            "window": self.tape.to_string(left, right),
            "steps": self.steps,
        }

    # ---------- internals ----------
    def _exec(self, instr: Instruction) -> None:
        op = instr.op
        # default next: same label, next index
        label, idx = self.pc
        next_pc = (label, idx + 1)

        if op is Op.MARK:
            self.tape.write(self.head, "1")
        elif op is Op.ERASE:
            self.tape.write(self.head, Tape.DEFAULT_BLANK)
        elif op is Op.R:
            self.head += 1
        elif op is Op.L:
            self.head -= 1
        elif op is Op.JZ:
            self._require_arg(instr)
            if self.tape.read(self.head) == Tape.DEFAULT_BLANK:
                next_pc = (instr.arg, 0)
        elif op is Op.JNZ:
            self._require_arg(instr)
            if self.tape.read(self.head) != Tape.DEFAULT_BLANK:
                next_pc = (instr.arg, 0)
        elif op is Op.GOTO:
            self._require_arg(instr)
            next_pc = (instr.arg, 0)
        elif op is Op.HALT:
            # set pc to end so subsequent step() returns False
            next_pc = (label, len(self.program.get_block(label)))
        else:  # pragma: no cover
            raise RuntimeError(f"Unsupported op: {op}")

        self.pc = next_pc

    @staticmethod
    def _require_arg(instr: Instruction) -> None:
        if not instr.arg:
            raise RuntimeError(f"{instr.op.name} requires label")
