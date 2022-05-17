import functions as func
import approximation as app
import draw


def main():
    fun = None
    while fun is None:
        fun = int(input("Choose function [1-7]: \n"
                        "1. Linear: 3x - 5\n"
                        "2. Absolute x: |x|\n"
                        "3. Polynomial: 2x^3 + 2x^2 + 4x - 1\n"
                        "4. Trigonometric: sin(1/x)\n"
                        "5. Composite #1: (2x + 3)^|x|\n"
                        "6. Composite #2: (2x + 3)(2x^3 + 2x^2 + 4x - 1)\n"
                        "7. Composite #3: sin(x)*|x|\n"))
        match fun:
            case 1:
                fun = func.linear
            case 2:
                fun = func.abs_x
            case 3:
                fun = func.polynomial
            case 4:
                fun = func.trigonometric
            case 5:
                fun = func.composite_1
            case 6:
                fun = func.composite_2
            case 7:
                fun = func.composite_3
            case _:
                fun = None

    l_range = float(input("Podaj dolny zakres: "))
    u_range = float(input("Podaj górny zakres: "))
    if l_range > u_range:
        pom = l_range
        l_range = u_range
        u_range = pom

    degree = int(input("Podaj stopień wielomianu: "))
    accuracy = float(input("Podaj dokładność: "))
    l_args = app.legendre_calculate_arguments(degree)
    factors = app.calculate_factors(fun, degree, l_range, u_range, accuracy, l_args)
    draw.draw_functions(l_range, u_range, fun, factors, l_args)
    # =====================Tests====================
    # # Func 1
    # fun1 = func.linear
    # l_range = -3
    # u_range = 5
    # degree = 2
    # accuracy = 0.0001
    # for i in range(4):
    #     l_args = app.legendre_calculate_arguments(degree)
    #     factors = app.calculate_factors(fun1, degree, l_range, u_range, accuracy, l_args)
    #     draw.draw_functions(l_range, u_range, fun1, factors, l_args)
    #     degree *= 2
    # # Func 2
    # fun2 = func.abs_x
    # l_range = -3
    # u_range = 5
    # degree = 2
    # accuracy = 0.0001
    # for i in range(4):
    #     l_args = app.legendre_calculate_arguments(degree)
    #     factors = app.calculate_factors(fun1, degree, l_range, u_range, accuracy, l_args)
    #     draw.draw_functions(l_range, u_range, fun1, factors, l_args)
    #     degree *= 2
    # # Func 3
    # fun3 = func.polynomial
    # l_range = -3
    # u_range = 5
    # degree = 2
    # accuracy = 0.0001
    # for i in range(4):
    #     l_args = app.legendre_calculate_arguments(degree)
    #     factors = app.calculate_factors(fun1, degree, l_range, u_range, accuracy, l_args)
    #     draw.draw_functions(l_range, u_range, fun1, factors, l_args)
    #     degree *= 2
    # # Func 4
    # fun4 = func.trigonometric
    # l_range = -3
    # u_range = 5
    # degree = 2
    # accuracy = 0.0001
    # for i in range(4):
    #     l_args = app.legendre_calculate_arguments(degree)
    #     factors = app.calculate_factors(fun1, degree, l_range, u_range, accuracy, l_args)
    #     draw.draw_functions(l_range, u_range, fun1, factors, l_args)
    #     degree *= 2
    # # Func 5
    # fun5 = func.composite_1
    # l_range = -1.5
    # u_range = .5
    # degree = 2
    # accuracy = 0.0001
    # for i in range(4):
    #     l_args = app.legendre_calculate_arguments(degree)
    #     factors = app.calculate_factors(fun1, degree, l_range, u_range, accuracy, l_args)
    #     draw.draw_functions(l_range, u_range, fun1, factors, l_args)
    #     degree *= 2
    # # Func 6
    # fun6 = func.composite_2
    # l_range = -2
    # u_range = 1
    # degree = 2
    # accuracy = 0.0001
    # for i in range(4):
    #     l_args = app.legendre_calculate_arguments(degree)
    #     factors = app.calculate_factors(fun1, degree, l_range, u_range, accuracy, l_args)
    #     draw.draw_functions(l_range, u_range, fun1, factors, l_args)
    #     degree *= 2
    # # Func 7
    # fun7 = func.composite_3
    # l_range = -5
    # u_range = 3
    # degree = 2
    # accuracy = 0.0001
    # for i in range(4):
    #     l_args = app.legendre_calculate_arguments(degree)
    #     factors = app.calculate_factors(fun1, degree, l_range, u_range, accuracy, l_args)
    #     draw.draw_functions(l_range, u_range, fun1, factors, l_args)
    #     degree *= 2


if __name__ == '__main__':
    main()

