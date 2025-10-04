"""
Minimal CLI to demo Vector operations.

Usage examples:
  python -m vector.cli len "1,2,3"
  python -m vector.cli add "1,2,3" "4,5,6"
  python -m vector.cli dot "1,0,0" "0,1,0"
  python -m vector.cli cos "1,0,0" "0,1,0"
  python -m vector.cli cross "1,0,0" "0,1,0"
"""
from __future__ import annotations

import argparse
from typing import Optional
from .Vector import Vector


class VectorCLI:
    """Class-based CLI for Vector operations."""

    # ---------- helpers ----------
    @staticmethod
    def parse_vec(s: str) -> Vector:
        return Vector.from_str(s)

    # ---------- command handlers ----------
    def cmd_len(self, args: argparse.Namespace) -> None:
        v = self.parse_vec(args.v)
        print(v.length())

    def cmd_add(self, args: argparse.Namespace) -> None:
        a, b = self.parse_vec(args.a), self.parse_vec(args.b)
        print(a + b)

    def cmd_sub(self, args: argparse.Namespace) -> None:
        a, b = self.parse_vec(args.a), self.parse_vec(args.b)
        print(a - b)

    def cmd_dot(self, args: argparse.Namespace) -> None:
        a, b = self.parse_vec(args.a), self.parse_vec(args.b)
        print(a * b)

    def cmd_cos(self, args: argparse.Namespace) -> None:
        a, b = self.parse_vec(args.a), self.parse_vec(args.b)
        print(a.cos(b))

    def cmd_cross(self, args: argparse.Namespace) -> None:
        a, b = self.parse_vec(args.a), self.parse_vec(args.b)
        print(a.cross(b))

    def cmd_scale(self, args: argparse.Namespace) -> None:
        a = self.parse_vec(args.a)
        print(a * args.k)

    def cmd_div(self, args: argparse.Namespace) -> None:
        a = self.parse_vec(args.a)
        print(a / args.k)

    # ---------- parser wiring ----------
    def build_parser(self) -> argparse.ArgumentParser:
        p = argparse.ArgumentParser(prog="vector", description="Vector demo CLI")
        sub = p.add_subparsers(dest="cmd", required=True)

        sp = sub.add_parser("len")
        sp.add_argument("v")
        sp.set_defaults(func=self.cmd_len)

        sp = sub.add_parser("add")
        sp.add_argument("a")
        sp.add_argument("b")
        sp.set_defaults(func=self.cmd_add)

        sp = sub.add_parser("sub")
        sp.add_argument("a")
        sp.add_argument("b")
        sp.set_defaults(func=self.cmd_sub)

        sp = sub.add_parser("dot")
        sp.add_argument("a")
        sp.add_argument("b")
        sp.set_defaults(func=self.cmd_dot)

        sp = sub.add_parser("cos")
        sp.add_argument("a")
        sp.add_argument("b")
        sp.set_defaults(func=self.cmd_cos)

        sp = sub.add_parser("cross")
        sp.add_argument("a")
        sp.add_argument("b")
        sp.set_defaults(func=self.cmd_cross)

        sp = sub.add_parser("scale")
        sp.add_argument("a")
        sp.add_argument("k", type=float)
        sp.set_defaults(func=self.cmd_scale)

        sp = sub.add_parser("div")
        sp.add_argument("a")
        sp.add_argument("k", type=float)
        sp.set_defaults(func=self.cmd_div)

        return p

    # ---------- entry ----------
    def run(self, argv: Optional[list[str]] = None) -> None:
        parser = self.build_parser()
        args = parser.parse_args(argv)
        args.func(args)


def main(argv: Optional[list[str]] = None) -> None:
    VectorCLI().run(argv)


if __name__ == "__main__":
    main()
