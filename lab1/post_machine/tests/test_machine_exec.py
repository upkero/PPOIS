import textwrap
from post_machine.Program import Program
from post_machine.Tape import Tape
from post_machine.PostMachine import PostMachine


def program_from_str(s: str) -> Program:
    import tempfile, os
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8", suffix=".txt") as f:
        f.write(textwrap.dedent(s))
        path = f.name
    prog = Program.from_file(path)
    os.unlink(path)
    return prog


def test_mark_move_halt():
    prog = program_from_str(
        """
        START: main
        [main]
        MARK
        R
        HALT
        """
    )
    m = PostMachine(program=prog, tape=Tape())
    m.reset(head=0, start_label="main")
    m.run()
    # after MARK at 0, head=1
    assert m.tape.read(0) == "1"
    assert m.head == 1


def test_loop_until_three_marks():
    # Put three '1' and halt
    prog = program_from_str(
        """
        START: main
        [main]
        MARK
        R
        MARK
        R
        MARK
        HALT
        """
    )
    t = Tape()
    m = PostMachine(program=prog, tape=t)
    m.reset(head=0, start_label="main")
    m.run(max_steps=100)  # защитный лимит, чтобы никогда не зависнуть
    assert t.to_string(0, 2) == "111"
