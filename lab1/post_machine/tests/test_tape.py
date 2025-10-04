from post_machine.Tape import Tape


def test_read_write_and_sparse():
    t = Tape()
    assert t.read(0) == Tape.DEFAULT_BLANK
    t.write(0, "1")
    assert t.read(0) == "1"
    t.write(0, Tape.DEFAULT_BLANK)
    assert t.read(0) == Tape.DEFAULT_BLANK


def test_bulk_load_and_window():
    t = Tape()
    t.bulk_load("__1_1")
    assert t.read(2) == "1"
    assert t.to_string(0, 4) == "__1_1"


def test_minmax_visits():
    t = Tape()
    _ = t.read(0)
    t.write(5, "1")
    t.write(-3, "1")
    mn, mx = t.minmax()
    assert mn <= -3 and mx >= 5
