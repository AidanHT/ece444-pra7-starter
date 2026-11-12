def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def broken_total(values):
    return sum(values)
