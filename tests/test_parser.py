"""Unit tests for expression parser."""

import pytest

from expression_parser import ExpressionParser


class TestExpressionParser:
    """Tests for the expression parser."""

    def setup_method(self):
        """Set up test fixtures."""
        self.parser = ExpressionParser()

    def test_single_number(self):
        """Test parsing a single number."""
        assert self.parser.parse("42") == 42
        assert self.parser.parse("3.14") == pytest.approx(3.14)

    def test_addition(self):
        """Test addition expressions."""
        assert self.parser.parse("1 + 2") == 3
        assert self.parser.parse("10 + 20") == 30
        assert self.parser.parse("1 + 2 + 3") == 6

    def test_subtraction(self):
        """Test subtraction expressions."""
        assert self.parser.parse("5 - 3") == 2
        assert self.parser.parse("10 - 20") == -10
        assert self.parser.parse("10 - 3 - 2") == 5

    def test_multiplication(self):
        """Test multiplication expressions."""
        assert self.parser.parse("2 * 3") == 6
        assert self.parser.parse("10 * 5") == 50
        assert self.parser.parse("2 * 3 * 4") == 24

    def test_division(self):
        """Test division expressions."""
        assert self.parser.parse("10 / 2") == 5
        assert self.parser.parse("15 / 3") == 5
        assert self.parser.parse("7 / 2") == 3.5

    def test_power(self):
        """Test power expressions."""
        assert self.parser.parse("2 ** 3") == 8
        assert self.parser.parse("3 ** 2") == 9
        assert self.parser.parse("2 ** 3 ** 2") == 512  # Right-associative: 2^(3^2)

    def test_operator_precedence(self):
        """Test operator precedence."""
        assert self.parser.parse("2 + 3 * 4") == 14
        assert self.parser.parse("2 * 3 + 4") == 10
        assert self.parser.parse("2 * 3 ** 2") == 18
        assert self.parser.parse("(2 + 3) * 4") == 20

    def test_parentheses(self):
        """Test parenthesized expressions."""
        assert self.parser.parse("(2 + 3) * 4") == 20
        assert self.parser.parse("2 * (3 + 4)") == 14
        assert self.parser.parse("((2 + 3) * 4) / 2") == 10

    def test_unary_minus(self):
        """Test unary minus operator."""
        assert self.parser.parse("-5") == -5
        assert self.parser.parse("-(3 + 2)") == -5
        assert self.parser.parse("1 + -2") == -1

    def test_sqrt_function(self):
        """Test sqrt function."""
        assert self.parser.parse("sqrt(9)") == 3
        assert self.parser.parse("sqrt(4)") == 2
        assert self.parser.parse("sqrt(2)") == pytest.approx(1.41421356)

    def test_complex_expressions(self):
        """Test complex multi-operator expressions."""
        assert self.parser.parse("1 + 2 - 4") == -1
        assert self.parser.parse("2 ** 3 + 1") == 9
        assert self.parser.parse("sqrt(16) + 2 * 3") == 10
        assert self.parser.parse("10 / 2 - 3") == 2

    def test_whitespace_handling(self):
        """Test that parser handles whitespace correctly."""
        assert self.parser.parse("1+2") == 3
        assert self.parser.parse("1 + 2") == 3
        assert self.parser.parse("1  +  2") == 3
        assert self.parser.parse("  1 + 2  ") == 3

    def test_float_numbers(self):
        """Test parsing and calculating with floats."""
        assert self.parser.parse("1.5 + 2.5") == 4.0
        assert self.parser.parse("3.14 * 2") == pytest.approx(6.28)
        assert self.parser.parse("10.5 / 2") == 5.25

    def test_division_by_zero_error(self):
        """Test that division by zero raises an error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.parser.parse("5 / 0")

    def test_sqrt_negative_error(self):
        """Test that sqrt of negative raises an error."""
        with pytest.raises(ValueError, match="Cannot take square root of negative"):
            self.parser.parse("sqrt(-4)")

    def test_invalid_expression_error(self):
        """Test that invalid expressions raise errors."""
        with pytest.raises(ValueError):
            self.parser.parse("1 +")  # Incomplete
        with pytest.raises(ValueError):
            self.parser.parse("(1 + 2")  # Missing closing paren
        with pytest.raises(ValueError):
            self.parser.parse("1 + * 2")  # Invalid operator sequence

    def test_tokenization(self):
        """Test the tokenization process."""
        tokens = self.parser.tokenize("1 + 2 * 3")
        assert len(tokens) == 6  # 1, +, 2, *, 3, EOF

    def test_power_right_associativity(self):
        """Test that power is right-associative."""
        # 2 ** 3 ** 2 should be 2 ** (3 ** 2) = 2 ** 9 = 512
        # NOT (2 ** 3) ** 2 = 8 ** 2 = 64
        assert self.parser.parse("2 ** 3 ** 2") == 512
