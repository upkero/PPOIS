import math
import pytest
from vector.Vector import Vector


def vclose(a: Vector, b: Vector, tol=1e-9):
    assert math.isclose(a.x, b.x, rel_tol=tol, abs_tol=1e-12)
    assert math.isclose(a.y, b.y, rel_tol=tol, abs_tol=1e-12)
    assert math.isclose(a.z, b.z, rel_tol=tol, abs_tol=1e-12)


def test_ctor_and_str():
    v = Vector(1, 2, 3)
    assert str(v) == "1 2 3"
    assert "Vector(" in repr(v)


def test_from_points():
    v = Vector.from_points((1, 1, 1), (4, 5, 9))
    vclose(v, Vector(3, 4, 8))


def test_from_str_spaces():
    assert Vector.from_str("1 2 3") == Vector(1, 2, 3)


def test_from_str_commas():
    assert Vector.from_str("1,2,3") == Vector(1, 2, 3)
    assert Vector.from_str("1, 2, 3") == Vector(1, 2, 3)


def test_length_and_normalized():
    v = Vector(3, 4, 0)
    assert math.isclose(v.length(), 5.0)
    vn = v.normalized()
    assert math.isclose(vn.length(), 1.0)
    vclose(vn * 5, v)


def test_add_sub():
    a = Vector(1, 2, 3)
    b = Vector(-1, 4, 0)
    vclose(a + b, Vector(0, 6, 3))
    vclose(a - b, Vector(2, -2, 3))


def test_scalar_mul_and_div():
    a = Vector(1.5, -2.0, 4.0)
    vclose(a * 2, Vector(3.0, -4.0, 8.0))
    vclose(2 * a, Vector(3.0, -4.0, 8.0))
    vclose(a / 2, Vector(0.75, -1.0, 2.0))


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = Vector(1, 2, 3) / 0.0


def test_dot_and_cross():
    i = Vector(1, 0, 0)
    j = Vector(0, 1, 0)
    k = Vector(0, 0, 1)
    assert i * i == 1
    assert i * j == 0
    vclose(i.cross(j), k)
    vclose(j.cross(k), i)
    vclose(k.cross(i), j)


def test_cos():
    i = Vector(1, 0, 0)
    j = Vector(0, 1, 0)
    assert math.isclose(i.cos(j), 0.0)
    assert math.isclose(i.cos(i), 1.0)
    with pytest.raises(ValueError):
        Vector(0, 0, 0).cos(i)


def test_comparisons_by_length():
    a = Vector(1, 0, 0)    # |a|=1
    b = Vector(1, 1, 0)    # |b|=sqrt(2)
    c = Vector(0.5, 0, 0)  # |c|=0.5
    assert a < b
    assert b > a
    assert c <= a
    assert a >= c
    assert not (a < c)
    assert not (c > a)


def test_equality_is_component_wise():
    a = Vector(1.0000000001, 2, 3)
    b = Vector(1.0, 2, 3)
    assert a == b  # tolerance-based equality


def test_iops_return_new_instances():
    a = Vector(1, 2, 3)
    b = Vector(1, 1, 1)
    c = a
    a += b
    assert a == Vector(2, 3, 4)
    assert c is not a  # immutability preserved
