import math

class Trig2(Operation):
    """Trig2 operation: cos(angle)."""

    def calculate(self, angle: float) -> float:
        """
        Calculate the cosine of an angle in radians.

        Args:
            angle: The angle in radians

        Returns:
            float: The cosine of the angle
        """
        return math.cos(angle)