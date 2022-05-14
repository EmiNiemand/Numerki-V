def newton_cotes(function, l_range: float, u_range: float, accuracy: float):
    last_result = 0
    i = 0

    while True:
        result = 0
        i += 1
        for j in range(i):
            # size of calculated subregion
            size = abs(l_range - u_range) / i
            result += calculate(function, l_range + size * j, l_range + size * (j + 1))

        # if difference smaller than accuracy return result
        if abs(result - last_result) < accuracy:
            return result

        last_result = result


def calculate(function, l_range: float, u_range: float):
    # https://ftims.edu.p.lodz.pl/pluginfile.php/186514/mod_resource/content/1/MNumOp%20wyk04%20_22.pdf
    # slajd 16
    h = (u_range - l_range) / 6
    return h * (function(l_range) + 4 * function((l_range + u_range) / 2) + function(u_range))

