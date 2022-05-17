import matplotlib.pyplot as mplot
import numpy as np
import newton_cotes as nc
import approximation as app


def draw_functions(lower_range: float, upper_range: float, function, factors, l_args):
    axes = mplot.figure().subplots()
    x = np.linspace(lower_range, upper_range, 100)
    y = []
    app_y = []
    for i in x:
        y.append(function(i))
        app_y.append(app.calculate_polynomial(i, lower_range, upper_range, factors, l_args))

    axes.plot(x, y, color="red", label="Original function")
    axes.plot(x, app_y, color="blue", label="Approximated function")

    def approximated(t): return app.calculate_polynomial(t, lower_range, upper_range, factors, l_args)
    def error_function(t): return abs(function(t) - approximated(t))

    error = nc.newton_cotes(error_function, lower_range, upper_range, 0.000001)

    mplot.title("Błąd aproksymacji: " + str(error))
    axes.set_xlabel('X')
    axes.set_ylabel('Y')

    mplot.show()

