import argparse


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


def get_coefficients(smoothing, order, offset, half_window):

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


def get_arguments():
    parser = argparse.ArgumentParser(description='Generate Savitsky-Golay filter coefficients for different parameters.')

    parser.add_argument('-ws', '--window_size',
                        help='Window size of the filter',
                        required=True, type=int)
    parser.add_argument('-o', '--order',
                        help='Order of the fit of the filter',
                        required=False, default=1, type=int)
    parser.add_argument('-s', '--smoothing',
                        help='Smoothing parameter. 0:polynomial smoothing, 1:first derivative, 2:second derivative, ...',
                        required=False, default=0, type=int)
    parser.add_argument('-t', '--offset',
                        help='Offset from the center point. 0:middle point, -window_size/2:last point, window_size/2 first point',
                        required=False, default=0, type=int)

    args = parser.parse_args()
    return args


if __name__ == "__main__":

    # Get command line arguments
    args = get_arguments()

    # Compute half of window_size (rounded down)
    half_window = args.window_size // 2

    # Print resulting coefficients to terminal
    print("[", end="")
    for i, coeff in enumerate(get_coefficients(args.smoothing, args.order, args.offset, half_window)):
        end = ", " if i < args.window_size - 1 else ""
        print(f"{coeff:0.5f}", end=end)
    print("]")
