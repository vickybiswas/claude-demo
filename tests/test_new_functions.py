import unittest
import math
from CAPS import LOG_UPPER, LOG_E, EXPONENT
from camel import Sine, Cosine
from snake import Root, Cube

class TestNewFunctions(unittest.TestCase):
    """Test suite for new calculator functions."""

    # CAPS Functions
    def test_log_upper(self):
        self.assertAlmostEqual(LOG_UPPER(100), 2.0)
        self.assertAlmostEqual(LOG_UPPER(1000), 3.0)
        with self.assertRaises(ValueError):
            LOG_UPPER(0)
        with self.assertRaises(ValueError):
            LOG_UPPER(-10)

    def test_log_e(self):
        self.assertAlmostEqual(LOG_E(math.e), 1.0)
        self.assertAlmostEqual(LOG_E(1), 0.0)
        with self.assertRaises(ValueError):
            LOG_E(0)
        with self.assertRaises(ValueError):
            LOG_E(-5)

    def test_exponent(self):
        self.assertEqual(EXPONENT(2, 3), 8)
        self.assertEqual(EXPONENT(5, 0), 1)
        self.assertEqual(EXPONENT(10, 2), 100)

    # camel Functions
    def test_sine(self):
        self.assertAlmostEqual(Sine(0), 0.0)
        self.assertAlmostEqual(Sine(math.pi/2), 1.0)
        self.assertAlmostEqual(Sine(math.pi), 0.0, places=5)

    def test_cosine(self):
        self.assertAlmostEqual(Cosine(0), 1.0)
        self.assertAlmostEqual(Cosine(math.pi/2), 0.0)
        self.assertAlmostEqual(Cosine(math.pi), -1.0)

    # snake Functions
    def test_root(self):
        self.assertAlmostEqual(Root(16), 4.0)
        self.assertAlmostEqual(Root(27, 3), 3.0)
        self.assertAlmostEqual(Root(81, 4), 3.0)
        with self.assertRaises(ValueError):
            Root(-4)  # Even root of negative
        self.assertAlmostEqual(Root(-8, 3), -2.0)  # Odd root of negative
        with self.assertRaises(ValueError):
            Root(16, 0)  # Non-positive degree

    def test_cube(self):
        self.assertEqual(Cube(2), 8)
        self.assertEqual(Cube(3), 27)
        self.assertEqual(Cube(-2), -8)
        self.assertEqual(Cube(0), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)