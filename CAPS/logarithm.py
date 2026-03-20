import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import math
from typing import Optional
from operation import Operation

class LOGARITHM(Operation):
    """Logarithm operation: log(x, base)."""

    def calculate(self, x: float, base: Optional[float] = math.e) -> float:
        """
        Calculate the logarithm of x with the specified base.

        Args:
            x: The number to calculate logarithm for (must be positive)
            base: The logarithm base (default: natural logarithm base e)

        Returns:
            float: The logarithm of x with the given base

        Raises:
            ValueError: If x is non-positive
        """
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        return math.log(x, base)