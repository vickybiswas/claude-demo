import unittest
import math
from CAPS import LOG_UPPER, LOG_E, EXPONENT
from camel import Sine, Cosine
from snake import Root, Cube

class TestNewFunctions(unittest.TestCase):
    """Test suite for new calculator functions."""

    # CAPS Functions
    def test_log_upper(self):
        log_upper = LOG_UPPER()
        self.assertAlmostEqual(log_upper.calculate(100), 2.0)
        self.assertAlmostEqual(log_upper.calculate(1000), 3.0)
        with self.assertRaises(ValueError):
            log_upper.calculate(0)
        with self.assertRaises(ValueError):
            log_upper.calculate(-10)

    def test_log_e(self):
        log_e = LOG_E()
        self.assertAlmostEqual(log_e.calculate(math.e), 1.0)
        self.assertAlmostEqual(log_e.calculate(1), 0.0)
        with self.assertRaises(ValueError):
            log_e.calculate(0)
        with self.assertRaises(ValueError):
            log_e.calculate(-5)

    def test_exponent(self):
        exp = EXPONENT()
        self.assertEqual(exp.calculate(2, 3), 8)
        self.assertEqual(exp.calculate(5, 0), 1)
        self.assertEqual(exp.calculate(10, 2), 100)

    # camel Functions
    def test_sine(self):
        sine = Sine()
        self.assertAlmostEqual(sine.calculate(0), 0.0)
        self.assertAlmostEqual(sine.calculate(math.pi/2), 1.0)
        self.assertAlmostEqual(sine.calculate(math.pi), 0.0, places=5)

    def test_cosine(self):
        cosine = Cosine()
        self.assertAlmostEqual(cosine.calculate(0), 1.0)
        self.assertAlmostEqual(cosine.calculate(math.pi/2), 0.0)
        self.assertAlmostEqual(cosine.calculate(math.pi), -1.0)

    # snake Functions
    def test_root(self):
        root = Root()
        self.assertAlmostEqual(root.calculate(16), 4.0)
        self.assertAlmostEqual(root.calculate(27, 3), 3.0)
        self.assertAlmostEqual(root.calculate(81, 4), 3.0)
        with self.assertRaises(ValueError):
            root.calculate(-4)  # Even root of negative
        self.assertAlmostEqual(root.calculate(-8, 3), -2.0)  # Odd root of negative
        with self.assertRaises(ValueError):
            root.calculate(16, 0)  # Non-positive degree

    def test_cube(self):
        cube = Cube()
        self.assertEqual(cube.calculate(2), 8)
        self.assertEqual(cube.calculate(3), 27)
        self.assertEqual(cube.calculate(-2), -8)
        self.assertEqual(cube.calculate(0), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)