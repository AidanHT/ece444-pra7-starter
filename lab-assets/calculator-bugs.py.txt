import os


def add(a,b):
    unused = 123
    return a + b


def record(value, history=[]):
    history.append(value)
    return history
