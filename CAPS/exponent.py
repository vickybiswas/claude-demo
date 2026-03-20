import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation

class EXPONENT(Operation):
    """Exponent operation: base ** exponent."""

    def calculate(self, base: float, exponent: float) -> float:
        """
        Raise a number to a power.

        Args:
            base: Base operand
            exponent: Exponent operand

        Returns:
            float: Result of base raised to the power of exponent
        """
        return base ** exponent