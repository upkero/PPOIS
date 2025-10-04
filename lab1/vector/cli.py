"""
Minimal CLI to demo Vector operations.

Usage examples:
  python -m vector.cli len "1,2,3"
  python -m vector.cli add "1,2,3" "4,5,6"
  python -m vector.cli dot "1,0,0" "0,1,0"
  python -m vector.cli cos "1,0,0" "0,1,0"
  python -m vector.cli cross "1,0,0" "0,1,0"
"""
import argparse
from .vector import Vector


def parse_vec(s: str) -> Vector:
    return Vector.from_str(s)


def cmd_len(args):
    v = parse_vec(args.v)
    print(v.length())


def cmd_add(args):
    a, b = parse_vec(args.a), parse_vec(args.b)
    print(a + b)


def cmd_sub(args):
    a, b = parse_vec(args.a), parse_vec(args.b)
    print(a - b)


def cmd_dot(args):
    a, b = parse_vec(args.a), parse_vec(args.b)
    print(a * b)


def cmd_cos(args):
    a, b = parse_vec(args.a), parse_vec(args.b)
    print(a.cos(b))


def cmd_cross(args):
    a, b = parse_vec(args.a), parse_vec(args.b)
    print(a.cross(b))


def cmd_scale(args):
    a = parse_vec(args.a)
    print(a * args.k)


def cmd_div(args):
    a = parse_vec(args.a)
    print(a / args.k)


def main():
    p = argparse.ArgumentParser(prog="vector", description="Vector demo CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("len")
    sp.add_argument("v")
    sp.set_defaults(func=cmd_len)

    sp = sub.add_parser("add")
    sp.add_argument("a")
    sp.add_argument("b")
    sp.set_defaults(func=cmd_add)

    sp = sub.add_parser("sub")
    sp.add_argument("a")
    sp.add_argument("b")
    sp.set_defaults(func=cmd_sub)

    sp = sub.add_parser("dot")
    sp.add_argument("a")
    sp.add_argument("b")
    sp.set_defaults(func=cmd_dot)

    sp = sub.add_parser("cos")
    sp.add_argument("a")
    sp.add_argument("b")
    sp.set_defaults(func=cmd_cos)

    sp = sub.add_parser("cross")
    sp.add_argument("a")
    sp.add_argument("b")
    sp.set_defaults(func=cmd_cross)

    sp = sub.add_parser("scale")
    sp.add_argument("a")
    sp.add_argument("k", type=float)
    sp.set_defaults(func=cmd_scale)

    sp = sub.add_parser("div")
    sp.add_argument("a")
    sp.add_argument("k", type=float)
    sp.set_defaults(func=cmd_div)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
