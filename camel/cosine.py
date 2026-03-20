"""Cosine operation with camelCase naming."""

import os
import sys
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class Cosine(Operation):
    """Cosine operation: cos(angle)."""

    def calculate(self, angle: float) -> float:
        """
        Calculate the cosine of an angle in radians.

        Args:
            angle: The angle in radians

        Returns:
            float: The cosine of the angle
        """
        return math.cos(angle)