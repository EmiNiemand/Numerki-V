from math import sin


def linear(x):
    return 3 * x - 5


def abs_x(x):
    return abs(x)


def polynomial(x):
    return ((2 * x + 2) * x + 4) * x - 1


def trigonometric(x):
    if x == 0:
        return 0
    return sin(1/x)


def composite_1(x):
    return (2 * x + 3) ** abs(x)


def composite_2(x):
    return (2 * x + 3) + ((2 * x + 2) * x + 4) * x - 1


def composite_3(x):
    return sin(x) * abs(x)

