"""Square root operation with snake_case naming."""

import os
import sys
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class SquareRoot(Operation):
    """Square root operation: sqrt(a)."""

    def calculate(self, operand: float) -> float:
        """
        Calculate the square root of a number.

        Args:
            operand: Number to take square root of

        Returns:
            float: Square root of the number

        Raises:
            ValueError: If operand is negative
        """
        if operand < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(operand)
