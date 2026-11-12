import pytest

from calculator import add, divide


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, 3) == 1


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero_returns_none():
    assert divide(1, 0) is None


def test_divide_wrong_type_raises():
    with pytest.raises(TypeError):
        divide("6", 3)
