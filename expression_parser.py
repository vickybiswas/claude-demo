"""Recursive descent expression parser for calculator expressions."""

import re
from enum import Enum, auto

from camel import Add, Multiply, Sine, Cosine
from CAPS import SUBTRACT, DIVIDE, EXPONENT, LOGARITHM, LOG_UPPER, LOG_E
from snake import Power, SquareRoot, Root, Cube


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
    COMMA = auto()
    FUNC = auto()
    EOF = auto()
    FUNC_LOG = auto()
    FUNC_LOG10 = auto()
    FUNC_LN = auto()
    FUNC_SIN = auto()
    FUNC_COS = auto()
    FUNC_TRIG1 = auto()
    FUNC_TRIG2 = auto()
    FUNC_ROOT = auto()
    FUNC_CUBE = auto()
    FUNC_EXP = auto()


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

    def __init__(self) -> None:
        """Initialize parser with operation instances."""
        self.add_op = Add()
        self.multiply_op = Multiply()
        self.subtract_op = SUBTRACT()
        self.divide_op = DIVIDE()
        self.power_op = Power()
        self.sqrt_op = SquareRoot()
        self.sin_op = Sine()
        self.cos_op = Cosine()
        self.exp_op = EXPONENT()
        self.log_op = LOGARITHM()
        self.log10_op = LOG_UPPER()
        self.ln_op = LOG_E()
        self.root_op = Root()
        self.cube_op = Cube()

        self.tokens: list[Token] = []
        self.position: int = 0

    def tokenize(self, expression) -> list[Token]:
        """
        Tokenize an expression into tokens.

        Args:
            expression: String expression to tokenize

        Returns:
            List of Token objects
        """
        self.tokens: list[Token] = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue

            # Check for function names
            if expression[i:].startswith("sqrt"):
                self.tokens.append(Token(TokenType.FUNC, "sqrt"))
                i += 4
            elif expression[i:].startswith("log"):
                self.tokens.append(Token(TokenType.FUNC_LOG, "log"))
                i += 3
            elif expression[i:].startswith("log10"):
                self.tokens.append(Token(TokenType.FUNC_LOG10, "log10"))
                i += 5
            elif expression[i:].startswith("ln"):
                self.tokens.append(Token(TokenType.FUNC_LN, "ln"))
                i += 2
            elif expression[i:].startswith("sin"):
                self.tokens.append(Token(TokenType.FUNC_SIN, "sin"))
                i += 3
            elif expression[i:].startswith("cos"):
                self.tokens.append(Token(TokenType.FUNC_COS, "cos"))
                i += 3
            elif expression[i:].startswith("trig1"):
                self.tokens.append(Token(TokenType.FUNC_TRIG1, "trig1"))
                i += 5
            elif expression[i:].startswith("trig2"):
                self.tokens.append(Token(TokenType.FUNC_TRIG2, "trig2"))
                i += 5
            elif expression[i:].startswith("root"):
                self.tokens.append(Token(TokenType.FUNC_ROOT, "root"))
                i += 4
            elif expression[i:].startswith("cube"):
                self.tokens.append(Token(TokenType.FUNC_CUBE, "cube"))
                i += 4
            elif expression[i:].startswith("exp"):
                self.tokens.append(Token(TokenType.FUNC_EXP, "exp"))
                i += 3
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
            elif expression[i] == ",":
                self.tokens.append(Token(TokenType.COMMA, ","))
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

    def parse(self, expression) -> float:
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

    def _current_token(self) -> Token:
        """Get the current token."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return Token(TokenType.EOF, None)

    def _peek_token(self, offset: int = 1) -> Token:
        """Peek at a future token."""
        pos = self.position + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return Token(TokenType.EOF, None)

    def _consume(self, expected_type: TokenType | None = None) -> Token:
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

    def _parse_addition(self) -> float:
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

    def _parse_multiplication(self) -> float:
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

        # Function calls
        if self._current_token().type == TokenType.FUNC:
            func_token = self._consume(TokenType.FUNC)
            self._consume(TokenType.LPAREN)
            arg = self._parse_addition()
            self._consume(TokenType.RPAREN)

            if func_token.value == "sqrt":
                return self.sqrt_op.calculate(arg)
            else:
                raise ValueError(f"Unknown function: {func_token.value}")
        elif self._current_token().type == TokenType.FUNC_LOG:
            self._consume(TokenType.FUNC_LOG)
            self._consume(TokenType.LPAREN)
            x = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.log_op.calculate(x)
        elif self._current_token().type == TokenType.FUNC_LOG10:
            self._consume(TokenType.FUNC_LOG10)
            self._consume(TokenType.LPAREN)
            x = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.log10_op.calculate(x)
        elif self._current_token().type == TokenType.FUNC_LN:
            self._consume(TokenType.FUNC_LN)
            self._consume(TokenType.LPAREN)
            x = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.ln_op.calculate(x)
        elif self._current_token().type == TokenType.FUNC_SIN:
            self._consume(TokenType.FUNC_SIN)
            self._consume(TokenType.LPAREN)
            angle = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.sin_op.calculate(angle)
        elif self._current_token().type == TokenType.FUNC_COS:
            self._consume(TokenType.FUNC_COS)
            self._consume(TokenType.LPAREN)
            angle = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.cos_op.calculate(angle)
        elif self._current_token().type == TokenType.FUNC_TRIG1:
            self._consume(TokenType.FUNC_TRIG1)
            self._consume(TokenType.LPAREN)
            angle = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.trig1_op.calculate(angle)
        elif self._current_token().type == TokenType.FUNC_TRIG2:
            self._consume(TokenType.FUNC_TRIG2)
            self._consume(TokenType.LPAREN)
            angle = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.trig2_op.calculate(angle)
        elif self._current_token().type == TokenType.FUNC_ROOT:
            self._consume(TokenType.FUNC_ROOT)
            self._consume(TokenType.LPAREN)
            value = self._parse_addition()
            self._consume(TokenType.COMMA)
            degree = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.root_op.calculate(value, int(degree))
        elif self._current_token().type == TokenType.FUNC_CUBE:
            self._consume(TokenType.FUNC_CUBE)
            self._consume(TokenType.LPAREN)
            value = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.cube_op.calculate(value)
        elif self._current_token().type == TokenType.FUNC_EXP:
            self._consume(TokenType.FUNC_EXP)
            self._consume(TokenType.LPAREN)
            base = self._parse_addition()
            self._consume(TokenType.COMMA)
            exponent = self._parse_addition()
            self._consume(TokenType.RPAREN)
            return self.exp_op.calculate(base, exponent)

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
