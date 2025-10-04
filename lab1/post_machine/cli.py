"""
CLI for Post Machine.

Examples:
  python -m post_machine.cli run program.txt --log
  python -m post_machine.cli run program.txt --tape-inline "___11_1" --head 0 --start main --max-steps 100
  python -m post_machine.cli inspect program.txt
  python -m post_machine.cli step program.txt --steps 5 --log
"""
import argparse
import sys
from typing import Optional

from .tape import Tape, DEFAULT_BLANK
from .program import Program, ProgramParseError
from .machine import PostMachine


def _load_tape(args, prog: Program) -> Tape:
    t = Tape()
    # priority: CLI inline/file > program meta TAPE
    if args.tape_inline is not None:
        t.bulk_load(args.tape_inline)
        return t
    if args.tape_file is not None:
        with open(args.tape_file, "r", encoding="utf-8") as f:
            s = f.read().strip()
        t.bulk_load(s)
        return t
    meta = prog.meta
    if meta.tape_inline is not None:
        t.bulk_load(meta.tape_inline)
    return t


def _resolve_head(args, prog: Program) -> int:
    if args.head is not None:
        return args.head
    if prog.meta.head is not None:
        return prog.meta.head
    return 0


def _resolve_start(args, prog: Program) -> str:
    if args.start is not None:
        return args.start
    if prog.meta.start_label is not None:
        return prog.meta.start_label
    return prog.labels()[0]


def _logger_factory(enabled: bool):
    def _log(state: dict):
        if not enabled:
            return
        pc = state["pc"]
        print(
            f"[step={state['steps']}] {pc['label']}#{pc['index']} "
            f"head={state['head']} cell={state['cell']} window='{state['window']}'"
        )
    return _log


def cmd_inspect(args):
    prog = Program.from_file(args.program)
    print("Labels:")
    for lbl in prog.labels():
        print(f"  - {lbl} ({len(prog.get_block(lbl))} instructions)")
    meta = prog.meta
    print("Meta:")
    print(f"  START: {meta.start_label}")
    print(f"  HEAD:  {meta.head}")
    print(f"  TAPE:  {meta.tape_inline!r}")


def _build_machine(args) -> PostMachine:
    prog = Program.from_file(args.program)
    tape = _load_tape(args, prog)
    head = _resolve_head(args, prog)
    start = _resolve_start(args, prog)
    m = PostMachine(program=prog, tape=tape)
    m.reset(head=head, start_label=start)
    return m


def cmd_run(args):
    m = _build_machine(args)
    logger = _logger_factory(args.log)
    m.run(max_steps=args.max_steps, logger=logger)


def cmd_step(args):
    m = _build_machine(args)
    logger = _logger_factory(args.log)
    steps = args.steps
    if steps <= 0:
        print("steps must be > 0", file=sys.stderr)
        sys.exit(2)
    m.run(max_steps=steps, logger=logger)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="post-machine", description="Post Machine CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("program", help="path to program file")
    common.add_argument("--tape-file", help="file with initial tape (string)")
    common.add_argument("--tape-inline", help="inline initial tape, e.g. ___11_1")
    common.add_argument("--head", type=int, help="initial head position")
    common.add_argument("--start", help="start label name")
    common.add_argument("-l", "--log", action="store_true", help="log state after each step")

    sp = sub.add_parser("inspect", parents=[common], help="show labels and meta")
    sp.set_defaults(func=cmd_inspect)

    sp = sub.add_parser("run", parents=[common], help="run until HALT or max steps")
    sp.add_argument("--max-steps", type=int, help="limit number of steps")
    sp.set_defaults(func=cmd_run)

    sp = sub.add_parser("step", parents=[common], help="execute N steps")
    sp.add_argument("--steps", type=int, default=1)
    sp.set_defaults(func=cmd_step)

    return p


def main(argv: Optional[list[str]] = None):
    p = build_parser()
    args = p.parse_args(argv)
    try:
        args.func(args)
    except ProgramParseError as e:
        print(f"Program parse error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
