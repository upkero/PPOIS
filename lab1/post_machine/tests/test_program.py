import textwrap
import pytest
from post_machine.Program import Program
from post_machine.exeptions import ProgramParseError


def make_prog(tmp_path, content: str):
    p = tmp_path / "prog.txt"
    p.write_text(textwrap.dedent(content), encoding="utf-8")
    return p


def test_parse_program_with_meta_and_blocks(tmp_path):
    path = make_prog(
        tmp_path,
        """
        # meta
        TAPE: ___11_
        HEAD: 2
        START: main

        [main]
        MARK
        R
        JNZ end
        L
        GOTO main

        [end]
        HALT
        """,
    )
    prog = Program.from_file(str(path))
    assert set(prog.labels()) == {"main", "end"}
    assert prog.meta.tape_inline == "___11_"
    assert prog.meta.head == 2
    assert prog.meta.start_label == "main"
    assert len(prog.get_block("main")) >= 1


def test_parse_errors(tmp_path):
    # instruction outside block
    path = make_prog(tmp_path, "MARK\n")
    with pytest.raises(ProgramParseError):
        Program.from_file(str(path))

    # duplicate label
    path = make_prog(
        tmp_path,
        """
        [a]
        HALT
        [a]
        HALT
        """,
    )
    with pytest.raises(ProgramParseError):
        Program.from_file(str(path))
