def hilbIndex(x, y, eps):
    # Parameter: x, y: coordinates of image point, x, y in [0, 1]^2
    # eps: required precision (of index parameter)

    if eps > 1:
        return 0

    if x < 0.5:
        if y < 0.5:
            return (0 + hilbIndex(2 * y, 2 * x, 4 * eps)) / 4
        else:
            return (1 + hilbIndex(2 * x, 2 * y - 1, 4 * eps)) / 4
    else:
        if y >= 0.5:
            return (2 + hilbIndex(2 * x - 1, 2 * y - 1, 4 * eps)) / 4
        else:
            return (3 + hilbIndex(1 - 2 * y, 2 - 2 * x, 4 * eps)) / 4
