import math

class Trig1(Operation):
    """Trig1 operation: sin(angle)."""

    def calculate(self, angle: float) -> float:
        """
        Calculate the sine of an angle in radians.

        Args:
            angle: The angle in radians

        Returns:
            float: The sine of the angle
        """
        return math.sin(angle)