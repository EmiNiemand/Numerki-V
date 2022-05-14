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
    factors = app.calculate_factors(fun, degree, l_range, u_range, .00001)
    draw.draw_functions(l_range, u_range, fun, factors)


if __name__ == '__main__':
    main()

