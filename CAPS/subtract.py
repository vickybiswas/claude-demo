"""Subtraction operation with UPPERCASE naming."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class SUBTRACT(Operation):
    """Subtraction operation: a - b."""

    def calculate(self, FIRST_NUMBER: float, SECOND_NUMBER: float = None) -> float:
        """
        Subtract two numbers.

        Args:
            FIRST_NUMBER: First operand (minuend)
            SECOND_NUMBER: Second operand (subtrahend)

        Returns:
            float: Difference of the two numbers
        """
        RESULT = FIRST_NUMBER - SECOND_NUMBER
        return RESULT