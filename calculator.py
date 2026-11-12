def add(a, b):
    return a + b


# B006 fix: a default like history=[] is created once when the function is
# defined and shared by every call. None is immutable, so it is a safe default.
def record(value, history=None):
    if history is None:  # use `is None`, not `== None` (E711)
        history = []  # new list on each call
    history.append(value)
    return history


# E722 fix (item 5): a bare `except:` caught everything, so divide("6", 3)
# returned None and hid the TypeError. Catch only the error we expect.
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:  # only b == 0; other errors still raise
        return None


# F821 fix (item 10): this used to return the undefined name `missing_total`.
# Ruff caught it, but the tests passed because no test called this function.
def broken_total(values):
    return sum(values)
