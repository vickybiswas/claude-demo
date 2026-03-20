import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import math
from operation import Operation

class LOG_UPPER(Operation):
    """Logarithm base-10 operation: log10(x)."""

    def calculate(self, x: float) -> float:
        """
        Calculate the base-10 logarithm of x.

        Args:
            x: The number to calculate logarithm for (must be positive)

        Returns:
            float: The base-10 logarithm of x

        Raises:
            ValueError: If x is non-positive
        """
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        return math.log10(x)