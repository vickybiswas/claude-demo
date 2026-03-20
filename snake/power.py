"""Power (exponentiation) operation with snake_case naming."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class Power(Operation):
    """Power operation: a ** b (exponentiation)."""

    def calculate(self, base_number, exponent_number=None):
        """
        Raise a number to a power.

        Args:
            base_number: Base operand
            exponent_number: Exponent operand

        Returns:
            float: Result of base raised to the power of exponent
        """
        calculated_result = base_number ** exponent_number
        return calculated_result
