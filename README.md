# Savitsky-Golay filter coefficients calculator

This repository contains a python implementation of the Savitsky-Golay filter coefficients calculation. This implementation is based on the Pascal implementation in the paper [General Least Squares Smoothing And Differentiation By The Convolution Method](http://www.personal.psu.edu/users/m/r/mrh318/Gorry-AC-1990.pdf). I needed access to the coefficients of the filter in python, and I hope this repo can be useful to someone.

# Installation

There are no dependencies to use this calculator. To install simply run:

```
    pip install savgol-calculator
```

# Usage

The script is very simple to use. Here is the help message:

```
    usage: savgol.py [-h] -ws WINDOW_SIZE [-o ORDER] [-s SMOOTHING] [-t OFFSET]

    Generate Savitsky-Golay filter coefficients for different parameters.

    optional arguments:
      -h, --help            show this help message and exit
      -ws WINDOW_SIZE, --window_size WINDOW_SIZE
                            Window size of the filter
      -o ORDER, --order ORDER
                            Order of the fit of the filter
      -s SMOOTHING, --smoothing SMOOTHING
                            Smoothing parameter. 0:polynomial smoothing, 1:first derivative, 2:second derivative, ...
      -t OFFSET, --offset OFFSET
                            Offset from the center point. 0:middle point, -window_size/2:last point, window_size/2 first point
```

For example, to get the coefficients of the filter for a window size of 5, a linear polynomial fit and with no offset (use the center point):

```
    python -m SGCC --window_size 5 --order 1 --smoothing 0 --offset 0
```

As another example, to get the coefficients of the filter for a window size of 101, a cubic polynomial fit, using the last point and computing the first derivative:

```
    python -m SGCC --window_size 101 --order 3 --smoothing 1 --offset -50
```

To get the coefficients in your application :

```
from SGCC.savgol import get_coefficients

# Compute the same coefficients as the examples above
coeffs = get_coefficients(smoothing=0,order=1,window_size=5,offset=0)
coeffs = get_coefficients(smoothing=1,order=3,window_size=101,offset=-50)
```

The function `get_coefficients` returns a list with the computed coefficients.

# Configuration

Here is the description of each parameter, taken from [here](http://www.users.waitrose.com/~robinjames/SG/parameters.html).

- window size, the number of points to be used for the estimate. Here, m is the number of points used on each side of the point in question. So for example if m = 3, the point in question is used plus three points on either side, so a total of 7 points are used in calculating the estimate.
    
- smoothing, the parameter to be estimated, which takes the following values:
        0 for smoothing
        1 for the first derivative (gradient)
        2 for the second derivative
        etc
    
- order, the order of the polynomial fit, specifically:
        1 for a linear (straight line) fit
        2 for a quadratic fit
        3 for a cubic fit
        etc
    
- offset, the offset from the centre point. Normally an equal number of points on either side of the point in question is used. However, this is not possible at the beginning and end of a series of readings. For these cases, coefficients for offsets from the centre point are given. The offset t is 0 for an estimate at the point in question, -1 for the previous point, -(half_window_size) for the first point, etc.


# Testing

To run the minimal tests, simply run:

```
python -m unittest test
```
