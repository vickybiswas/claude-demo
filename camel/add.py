"""Addition operation with camelCase naming."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class Add(Operation):
    """Addition operation: a + b."""

    def calculate(self, firstNumber, secondNumber=None):
        """
        Add two numbers.

        Args:
            firstNumber: First operand
            secondNumber: Second operand

        Returns:
            float: Sum of the two numbers
        """
        calculatedResult = firstNumber + secondNumber
        return calculatedResult
