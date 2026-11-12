# Import order (third-party, blank line, local) is enforced by the I rules (I001).
import pytest

from calculator import add, broken_total, divide


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, 3) == 1


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero_returns_none():  # the one error divide() should handle
    assert divide(1, 0) is None


# Fails with a bare `except:` (it would return None), passes after the E722 fix.
def test_divide_wrong_type_raises():
    with pytest.raises(TypeError):  # passes only if TypeError is raised inside
        divide("6", 3)


def test_broken_total_sums_values():  # added with the F821 fix
    assert broken_total([1, 2, 3]) == 6
