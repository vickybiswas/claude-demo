"""Recursive descent expression parser for calculator expressions."""

import re
from enum import Enum, auto

from camel import Add, Multiply
from CAPS import Subtract, Divide
from snake import Power, SquareRoot


class TokenType(Enum):
    """Token types for the lexer."""

    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()
    LPAREN = auto()
    RPAREN = auto()
    FUNC = auto()
    EOF = auto()


class Token:
    """Represents a single token."""

    def __init__(self, token_type, value):
        """Initialize a token."""
        self.type = token_type
        self.value = value

    def __repr__(self):
        """String representation of token."""
        return f"Token({self.type}, {self.value})"


class ExpressionParser:
    """Recursive descent parser for arithmetic expressions."""

    def __init__(self):
        """Initialize parser with operation instances."""
        self.add_op = Add()
        self.multiply_op = Multiply()
        self.subtract_op = Subtract()
        self.divide_op = Divide()
        self.power_op = Power()
        self.sqrt_op = SquareRoot()

        self.tokens = []
        self.position = 0

    def tokenize(self, expression):
        """
        Tokenize an expression into tokens.

        Args:
            expression: String expression to tokenize

        Returns:
            List of Token objects
        """
        self.tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue

            # Check for function names
            if expression[i:].startswith("sqrt"):
                self.tokens.append(Token(TokenType.FUNC, "sqrt"))
                i += 4
            # Check for ** operator
            elif i + 1 < len(expression) and expression[i : i + 2] == "**":
                self.tokens.append(Token(TokenType.POWER, "**"))
                i += 2
            # Single character tokens
            elif expression[i] == "+":
                self.tokens.append(Token(TokenType.PLUS, "+"))
                i += 1
            elif expression[i] == "-":
                self.tokens.append(Token(TokenType.MINUS, "-"))
                i += 1
            elif expression[i] == "*":
                self.tokens.append(Token(TokenType.MULTIPLY, "*"))
                i += 1
            elif expression[i] == "/":
                self.tokens.append(Token(TokenType.DIVIDE, "/"))
                i += 1
            elif expression[i] == "(":
                self.tokens.append(Token(TokenType.LPAREN, "("))
                i += 1
            elif expression[i] == ")":
                self.tokens.append(Token(TokenType.RPAREN, ")"))
                i += 1
            # Numbers
            elif expression[i].isdigit() or expression[i] == ".":
                match = re.match(r"\d+(\.\d+)?", expression[i:])
                if match:
                    num_str = match.group(0)
                    self.tokens.append(Token(TokenType.NUMBER, float(num_str)))
                    i += len(num_str)
                else:
                    i += 1
            else:
                i += 1

        self.tokens.append(Token(TokenType.EOF, None))
        return self.tokens

    def parse(self, expression):
        """
        Parse and evaluate an expression.

        Args:
            expression: String expression to parse

        Returns:
            float: Result of the evaluation
        """
        self.tokenize(expression)
        self.position = 0
        result = self._parse_addition()
        if self.position < len(self.tokens) - 1:
            raise ValueError(f"Unexpected token at position {self.position}")
        return result

    def _current_token(self):
        """Get the current token."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return Token(TokenType.EOF, None)

    def _peek_token(self, offset=1):
        """Peek at a future token."""
        pos = self.position + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return Token(TokenType.EOF, None)

    def _consume(self, expected_type=None):
        """Consume the current token and move to the next."""
        token = self._current_token()
        if expected_type and token.type != expected_type:
            raise ValueError(
                f"Expected {expected_type}, got {token.type} at position {self.position}"
            )
        self.position += 1
        return token

    # Operator precedence levels (lowest to highest):
    # 1. Addition/Subtraction
    # 2. Multiplication/Division
    # 3. Power (right-associative)
    # 4. Unary minus, functions, parentheses

    def _parse_addition(self):
        """Parse addition and subtraction (lowest precedence)."""
        left = self._parse_multiplication()

        while self._current_token().type in (TokenType.PLUS, TokenType.MINUS):
            op_token = self._consume()
            right = self._parse_multiplication()

            if op_token.type == TokenType.PLUS:
                left = self.add_op.calculate(left, right)
            else:  # MINUS
                left = self.subtract_op.calculate(left, right)

        return left

    def _parse_multiplication(self):
        """Parse multiplication and division."""
        left = self._parse_power()

        while self._current_token().type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op_token = self._consume()
            right = self._parse_power()

            if op_token.type == TokenType.MULTIPLY:
                left = self.multiply_op.calculate(left, right)
            else:  # DIVIDE
                left = self.divide_op.calculate(left, right)

        return left

    def _parse_power(self):
        """Parse power (right-associative)."""
        left = self._parse_unary()

        # Right-associative: a ** b ** c = a ** (b ** c)
        if self._current_token().type == TokenType.POWER:
            self._consume(TokenType.POWER)
            right = self._parse_power()  # Right-recursive for right-associativity
            left = self.power_op.calculate(left, right)

        return left

    def _parse_unary(self):
        """Parse unary operators and functions."""
        # Unary minus
        if self._current_token().type == TokenType.MINUS:
            self._consume(TokenType.MINUS)
            operand = self._parse_unary()
            return self.subtract_op.calculate(0, operand)

        # Function call (sqrt)
        if self._current_token().type == TokenType.FUNC:
            func_token = self._consume(TokenType.FUNC)
            self._consume(TokenType.LPAREN)
            arg = self._parse_addition()
            self._consume(TokenType.RPAREN)

            if func_token.value == "sqrt":
                return self.sqrt_op.calculate(arg)
            else:
                raise ValueError(f"Unknown function: {func_token.value}")

        # Primary (number or parenthesized expression)
        return self._parse_primary()

    def _parse_primary(self):
        """Parse primary expressions (numbers and parenthesized expressions)."""
        if self._current_token().type == TokenType.NUMBER:
            token = self._consume(TokenType.NUMBER)
            return token.value

        if self._current_token().type == TokenType.LPAREN:
            self._consume(TokenType.LPAREN)
            result = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return result

        raise ValueError(
            f"Expected number or '(', got {self._current_token().type}"
            f" at position {self.position}"
        )
