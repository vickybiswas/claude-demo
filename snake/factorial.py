"""Factorial operation with snake_case naming."""

import math

def factorial(integer: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if not isinstance(integer, int) or integer < 0:
        raise ValueError("Factorial only defined for non-negative integers")
    return math.factorial(integer)