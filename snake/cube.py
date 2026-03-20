"""Cube operation with snake_case naming."""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class Cube(Operation):
    """Cube operation: x^3."""

    def calculate(self, value: float) -> float:
        """
        Calculate the cube of a number.

        Args:
            value: The number to cube

        Returns:
            float: The cube of the value
        """
        return value ** 3