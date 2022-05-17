from newton_cotes import newton_cotes


def horner(x, arguments):
    result = arguments[0]
    for a in arguments[1:]:
        result = result * x + a

    return result


def legendre_calculate_arguments(degree: int) -> list[list[float]]:
    arguments = legendre_calculate_new_arguments()
    for i in range(degree):
        arguments = legendre_calculate_new_arguments(arguments)

    for j in range(len(arguments)):
        arguments[j] = list(reversed(arguments[j]))
    return arguments


def legendre_calculate_new_arguments(arguments: list[list[float]] = None) -> [list[list[float]]]:
    if arguments is None:
        return [[1.]]
    if len(arguments) == 1:
        arguments.append([0., 1.])
        return arguments

    degree = len(arguments)
    arguments.append([0. for _ in range(degree + 1)])

    for j in range(1, degree + 1):
        arguments[degree][j] = (2 * degree - 1) / degree * arguments[degree - 1][j - 1]

    for j in range(degree - 1):
        arguments[degree][j] -= (degree - 1) / degree * arguments[degree - 2][j]

    return arguments


def calculate_polynomial(x: float, l_range: float, u_range: float, args: [], l_args):
    result = 0
    n = 0
    for argument in args:
        result += argument * horner(transform_x(x, l_range, u_range), l_args[n])
        n += 1

    return result


def calculate_factors(function, degree: int, l_range: float, u_range: float, accuracy: float, l_args):
    result = []
    for k in range(degree):

        def new_function(t):
            x = transform_t(t, l_range, u_range)
            return function(x) * horner(t, l_args[k])

        factor = (2 * k + 1) / 2
        polynomial_factor = factor * newton_cotes(new_function, -1, 1, accuracy)
        result.append(polynomial_factor)

    return result


# scale < -1, 1 > to < a, b >
def transform_t(t, a, b):
    return ((b - a) * t + (a + b)) / 2


# scale < a,b > to < -1, 1 >
def transform_x(x, a, b):
    return (2 * x - a - b) / (b - a)

