"""Sine operation with camelCase naming."""

import os
import sys
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class Sine(Operation):
    """Sine operation: sin(angle)."""

    def calculate(self, angle: float) -> float:
        """
        Calculate the sine of an angle in radians.

        Args:
            angle: The angle in radians

        Returns:
            float: The sine of the angle
        """
        return math.sin(angle)