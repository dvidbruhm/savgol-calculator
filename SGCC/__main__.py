import argparse

from SGCC.savgol import get_coefficients


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

    print("Computing Savitsky-Golay filter coefficients with parameters:")
    print(f"\t-Window size: {args.window_size}")
    print(f"\t-Polynomial fit order: {args.order}")
    print(f"\t-Offset from center point: {args.offset}")
    print(f"\t-Estimation parameter: {args.smoothing} (0:smoothing, 1:first derivative, ...)")
    print()
    print("Filter coefficients:")

    # Print resulting coefficients to terminal
    print("[", end="")
    for i, coeff in enumerate(get_coefficients(args.smoothing, args.order, args.window_size, args.offset)):
        end = ", " if i < args.window_size - 1 else ""
        print(f"{coeff:0.5f}", end=end)
    print("]")
