def gram_poly(i, m, k, s):
    if k > 0:
        grampoly = (4 * k - 2) / (k * (2 * m - k + 1)) * (i * gram_poly(i, m, k - 1, s) + s * gram_poly(i, m, k - 1, s - 1)) - ((k - 1) * (2 * m + k)) / (k * (2 * m - k + 1)) * gram_poly(i, m, k - 2, s)
        return grampoly
    else:
        if k == 0 and s == 0:
            grampoly = 1
        else:
            grampoly = 0
        return grampoly


def gen_fact(a, b):
    gf = 1
    for j in range(a - b + 1, a + 1):
        gf = gf * j
    return gf


def coefficient(i, t, m, n, s):
    su = 0
    for k in range(0, n + 1):
        su = su + (2 * k + 1) * (gen_fact(2 * m, k) / gen_fact(2 * m + k + 1, k + 1)) * gram_poly(i, m, k, 0) * gram_poly(t, m, k, s)
    return su


def get_coefficients(smoothing, order, window_size, offset):

    # Compute half of window_size (rounded down)
    half_window = window_size // 2

    # Simple checks for input parameters
    assert half_window > 0, \
           "The window size has to be positive and greater than 0."
    assert offset <= half_window, \
           "Offset parameter can't be higher than window_size / 2. Current offset value: {args.offset}, current window_size value: {args.window_size}."
    assert offset >= -half_window, \
           "Offset parameter can't be lower than window_size / 2. Current offset value: {args.offset}, current window_size value: {args.window_size}."
    assert smoothing >= 0, \
           "Smoothing parameter has to be positive. Current value: {args.smoothing}"
    assert order > 0, \
           "Order has to be 1 or higher."

    coeffs = []
    for i in range(-half_window, half_window + 1):
        coeff = coefficient(offset, i, half_window, order, smoothing)
        coeffs.append(coeff)
    return coeffs
