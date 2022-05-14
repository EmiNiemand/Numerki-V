from newton_cotes import newton_cotes


def horner(x, arguments):
    result = arguments[0]
    for a in arguments[1:]:
        result = result * x + a

    return result


def legendre_polynomial(x: float, degree: int):
    previous_p = 1
    p = x

    if degree == 0:
        return previous_p
    elif degree == 1:
        return p

    for n in range(1, degree):
        next_p = ((2 * n + 1) / (n + 1) * x * p) - (n / (n + 1) * previous_p)
        previous_p = p
        p = next_p

    return p


def calculate_approximated_polynomial(x: float, l_range: float, u_range: float, args: []):
    result = 0
    n = 0
    for argument in args:
        result += argument * legendre_polynomial(transform_x(x, l_range, u_range), n)
        n += 1

    return result


def calculate_factors(function, degree: int, l_range: float, u_range: float, accuracy: float):
    result = []
    for k in range(degree):

        def new_function(t):
            x = transform_t(t, l_range, u_range)
            return function(x) * legendre_polynomial(t, k)

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

