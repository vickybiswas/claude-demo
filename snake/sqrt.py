"""Square root operation with snake_case naming."""

import os
import sys
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class SquareRoot(Operation):
    """Square root operation: sqrt(a)."""

    def calculate(self, operand_number, unused=None):
        """
        Calculate the square root of a number.

        Args:
            operand_number: Number to take square root of
            unused: Unused parameter (for interface compatibility)

        Returns:
            float: Square root of the number

        Raises:
            ValueError: If operand is negative
        """
        if operand_number < 0:
            raise ValueError("Cannot take square root of negative number")
        calculated_result = math.sqrt(operand_number)
        return calculated_result
