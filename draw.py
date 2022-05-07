import matplotlib.pyplot as mplot
import numpy as np
from sklearn import metrics
import approximation as app

def draw_functions(lower_range: float, upper_range: float, function, factors: [], n: int):
    axes = mplot.figure().subplots()
    x = np.linspace(lower_range, upper_range, 100)
    y = []
    app_y = []
    for i in x:
        y.append(function(i))
     #   app_y.append((app.polynomial_value(n, i, factors)))

    axes.plot(x, y, color="red", label="Original function")
    axes.plot(x, app_y, color="blue", label="Approximated function")

    r2 = round(100 * metrics.r2_score(y, app_y))
    mplot.title("Dokładność interpolacji: " + str(r2))
    axes.set_xlabel('X')
    axes.set_ylabel('Y')

    mplot.show()

