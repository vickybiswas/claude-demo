"""Division operation with UPPERCASE naming."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operation import Operation


class DIVIDE(Operation):
    """Division operation: a / b."""

    def calculate(self, FIRST_NUMBER: float, SECOND_NUMBER: float = None) -> float:
        """
        Divide two numbers.

        Args:
            FIRST_NUMBER: First operand (dividend)
            SECOND_NUMBER: Second operand (divisor)

        Returns:
            float: Quotient of the two numbers

        Raises:
            ValueError: If dividing by zero
        """
        if SECOND_NUMBER == 0:
            raise ValueError("Cannot divide by zero")
        RESULT = FIRST_NUMBER / SECOND_NUMBER
        return RESULT