import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import math
from operation import Operation

class LOG_E(Operation):
    """Natural logarithm operation: ln(x)."""

    def calculate(self, x: float) -> float:
        """
        Calculate the natural logarithm of x.

        Args:
            x: The number to calculate natural logarithm for (must be positive)

        Returns:
            float: The natural logarithm (base e) of x

        Raises:
            ValueError: If x is non-positive
        """
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        return math.log(x)