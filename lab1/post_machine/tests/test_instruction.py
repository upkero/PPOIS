import pytest
from post_machine.Instruction import Instruction
from post_machine.Op import Op


def test_simple_ops():
    assert Instruction.parse("MARK").op is Op.MARK
    assert Instruction.parse("ERASE").op is Op.ERASE
    assert Instruction.parse("R").op is Op.R
    assert Instruction.parse("L").op is Op.L
    assert Instruction.parse("HALT").op is Op.HALT


def test_jump_ops():
    j = Instruction.parse("JZ start")
    assert j.op is Op.JZ and j.arg == "start"
    j = Instruction.parse("JNZ loop")
    assert j.op is Op.JNZ and j.arg == "loop"
    j = Instruction.parse("GOTO end")
    assert j.op is Op.GOTO and j.arg == "end"


def test_parse_errors():
    with pytest.raises(ValueError):
        Instruction.parse("")
    with pytest.raises(ValueError):
        Instruction.parse("JZ")      # missing arg
    with pytest.raises(ValueError):
        Instruction.parse("GOTO a b")  # too many args
    with pytest.raises(ValueError):
        Instruction.parse("UNKNOWN")
    