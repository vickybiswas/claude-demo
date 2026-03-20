"""Root operation with snake_case naming."""

import os
import sys
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class Root(Operation):
    """Root operation: nth root of a number."""

    def calculate(self, value: float, degree: int = 2) -> float:
        """
        Calculate the nth root of a number.

        Args:
            value: The number to take the root of
            degree: The root degree (default: 2 for square root)

        Returns:
            float: The nth root of the value

        Raises:
            ValueError: If even root of negative number or non-positive degree
        """
        if value < 0 and degree % 2 == 0:
            raise ValueError("Cannot take even root of negative number")
        if value < 0 and degree % 2 != 0:
            return -((-value) ** (1/degree))
        if degree <= 0:
            raise ValueError("Root degree must be positive")
        return value ** (1/degree)