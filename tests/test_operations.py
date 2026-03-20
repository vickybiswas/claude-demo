"""Unit tests for calculator operations."""

import pytest

from camel import Add, Multiply
from CAPS import Subtract, Divide
from snake import Power, SquareRoot


class TestAdd:
    """Tests for Add operation."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        add = Add()
        assert add.calculate(1, 2) == 3

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        add = Add()
        assert add.calculate(-1, -2) == -3

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        add = Add()
        assert add.calculate(5, -3) == 2

    def test_add_zero(self):
        """Test adding zero."""
        add = Add()
        assert add.calculate(5, 0) == 5

    def test_add_floats(self):
        """Test adding floating-point numbers."""
        add = Add()
        assert add.calculate(1.5, 2.5) == 4.0


class TestMultiply:
    """Tests for Multiply operation."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        mult = Multiply()
        assert mult.calculate(3, 4) == 12

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        mult = Multiply()
        assert mult.calculate(-3, -4) == 12

    def test_multiply_mixed_signs(self):
        """Test multiplying numbers with different signs."""
        mult = Multiply()
        assert mult.calculate(3, -4) == -12

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        mult = Multiply()
        assert mult.calculate(5, 0) == 0

    def test_multiply_floats(self):
        """Test multiplying floating-point numbers."""
        mult = Multiply()
        assert mult.calculate(2.5, 4.0) == 10.0


class TestSubtract:
    """Tests for Subtract operation."""

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        sub = Subtract()
        assert sub.calculate(5, 3) == 2

    def test_subtract_negative_result(self):
        """Test subtraction that results in negative."""
        sub = Subtract()
        assert sub.calculate(3, 5) == -2

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        sub = Subtract()
        assert sub.calculate(-3, -5) == 2

    def test_subtract_zero(self):
        """Test subtracting zero."""
        sub = Subtract()
        assert sub.calculate(5, 0) == 5

    def test_subtract_floats(self):
        """Test subtracting floating-point numbers."""
        sub = Subtract()
        assert sub.calculate(5.5, 2.5) == 3.0


class TestDivide:
    """Tests for Divide operation."""

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        div = Divide()
        assert div.calculate(10, 2) == 5

    def test_divide_with_float_result(self):
        """Test division that results in a float."""
        div = Divide()
        assert div.calculate(5, 2) == 2.5

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        div = Divide()
        assert div.calculate(-10, -2) == 5

    def test_divide_mixed_signs(self):
        """Test dividing numbers with different signs."""
        div = Divide()
        assert div.calculate(-10, 2) == -5

    def test_divide_by_zero(self):
        """Test that dividing by zero raises error."""
        div = Divide()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            div.calculate(5, 0)

    def test_divide_floats(self):
        """Test dividing floating-point numbers."""
        div = Divide()
        assert div.calculate(7.5, 2.5) == 3.0


class TestPower:
    """Tests for Power operation."""

    def test_power_basic(self):
        """Test basic power operation."""
        power = Power()
        assert power.calculate(2, 3) == 8

    def test_power_zero_exponent(self):
        """Test any number to the power of 0."""
        power = Power()
        assert power.calculate(5, 0) == 1

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        power = Power()
        assert power.calculate(2, -1) == 0.5

    def test_power_float_base(self):
        """Test power with float base."""
        power = Power()
        assert power.calculate(2.5, 2) == 6.25

    def test_power_float_exponent(self):
        """Test power with float exponent."""
        power = Power()
        assert power.calculate(4, 0.5) == 2.0


class TestSquareRoot:
    """Tests for SquareRoot operation."""

    def test_sqrt_perfect_square(self):
        """Test square root of a perfect square."""
        sqrt = SquareRoot()
        assert sqrt.calculate(9) == 3

    def test_sqrt_one(self):
        """Test square root of 1."""
        sqrt = SquareRoot()
        assert sqrt.calculate(1) == 1

    def test_sqrt_zero(self):
        """Test square root of 0."""
        sqrt = SquareRoot()
        assert sqrt.calculate(0) == 0

    def test_sqrt_non_perfect_square(self):
        """Test square root of non-perfect square."""
        sqrt = SquareRoot()
        result = sqrt.calculate(2)
        assert abs(result - 1.41421356) < 0.0001

    def test_sqrt_float(self):
        """Test square root of float."""
        sqrt = SquareRoot()
        assert sqrt.calculate(6.25) == 2.5

    def test_sqrt_negative(self):
        """Test that square root of negative number raises error."""
        sqrt = SquareRoot()
        with pytest.raises(ValueError, match="Cannot take square root of negative"):
            sqrt.calculate(-4)
