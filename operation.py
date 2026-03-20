"""Abstract base class for calculator operations."""

from abc import ABC, abstractmethod


class Operation(ABC):
    """Base class for all calculator operations."""

    @abstractmethod
    def calculate(self, a: float, b: float | None = None) -> float:
        """
        Perform the operation.

        Args:
            a: First operand
            b: Second operand (optional for unary operations)

        Returns:
            float: Result of the operation
        """
        pass
