import unittest

from savgol_poly import get_coefficients


class TestSavGol(unittest.TestCase):
    def test_linear_smoothing_no_offset(self):
        smoothing, order, half_window, offset = 0, 1, 1, 0
        coeffs = get_coefficients(smoothing, order, offset, half_window)
        self.assertEqual([round(c, 2) for c in coeffs], [0.33, 0.33, 0.33])

    def test_quadratic_smoothing_no_offset(self):
        smoothing, order, half_window, offset = 0, 2, 2, 0
        coeffs = get_coefficients(smoothing, order, offset, half_window)
        self.assertEqual([round(c, 2) for c in coeffs], [-0.09, 0.34, 0.49, 0.34, -0.09])

    def test_linear_smoothing_with_offset(self):
        smoothing, order, half_window, offset = 0, 1, 2, 1
        coeffs = get_coefficients(smoothing, order, offset, half_window)
        self.assertEqual([round(c, 2) for c in coeffs], [0.0, 0.1, 0.2, 0.3, 0.4])

    def test_wrong_input_params(self):
        smoothing, order, half_window, offset = 0, 1, 2, 3
        with self.assertRaises(AssertionError):
            get_coefficients(smoothing, order, offset, half_window)


if __name__ == '__main__':
    unittest.main()
