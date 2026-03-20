"""Multiplication operation with camelCase naming."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class Multiply(Operation):
    """Multiplication operation: a * b."""

    def calculate(self, firstNumber: float, secondNumber: float) -> float:
        """
        Multiply two numbers.

        Args:
            firstNumber: First operand
            secondNumber: Second operand

        Returns:
            float: Product of the two numbers
        """
        return firstNumber * secondNumber