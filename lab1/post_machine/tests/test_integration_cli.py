import textwrap
from post_machine.PostMachineCLI import main as cli_main


def make_prog(tmp_path, content: str):
    p = tmp_path / "prog.txt"
    p.write_text(textwrap.dedent(content), encoding="utf-8")
    return str(p)


def test_cli_inspect(monkeypatch, capsys, tmp_path):
    path = make_prog(
        tmp_path,
        """
        START: main
        TAPE: ___
        HEAD: 1

        [main]
        MARK
        HALT
        """,
    )
    cli_main(["inspect", path])
    out = capsys.readouterr().out
    assert "Labels:" in out and "main" in out
    assert "START:" in out and "HEAD:" in out


def test_cli_run_and_step(monkeypatch, capsys, tmp_path):
    path = make_prog(
        tmp_path,
        """
        START: main
        [main]
        MARK
        R
        HALT
        """,
    )
    # step 1
    cli_main(["step", path, "--steps", "1", "--log"])
    out = capsys.readouterr().out
    assert "step=1" in out

    # run (should HALT quickly)
    cli_main(["run", path, "--log"])
    out = capsys.readouterr().out
    # Should print at least one step line
    assert "step=" in out
