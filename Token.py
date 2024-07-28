from enum import auto, StrEnum
from typing import Optional

from symbol import Symbol

KEYWORDS = ['null', 'true', 'false', 'and', 'or', 'not', 'in', 'function']

class TokenType(StrEnum):
    VALUE = auto()  # ex: true, false, null
    NAME = auto()  # represents a key in json object
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    # VARIABLE = auto()  # custom variable or pre-defined must start with $
    LITERAL = auto()



class TokenKind(StrEnum):

    # Basic tokens
    STRING = auto()
    NUMBER = auto()
    BOOLEAN = auto()
    NULL = auto()
    LITERAL = auto()
    
    # Multi use Operators
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    LEFT_PARENTHESIS = auto()
    RIGHT_PARENTHESIS = auto()
    COMMA = auto()
    COLON = auto()
    ASTERISK = auto()
    PERCENTAGE = auto()
    FORWARD_SLASH = auto()
    DOLLAR = auto()
    EOF = auto()
    
    # Arithmetic Operators
    PLUS = auto()
    HYPHEN = auto()
    RANGE = auto()

    # Comparison Operators
    EQUAL = auto()
    NOTEQUAL = auto()
    LT = auto()
    GT = auto()
    LEQ = auto()
    GEQ = auto()
    IN = auto()

    # Logical Operators
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # Path Operators
    DOT = auto()
    CARET = auto()
    DESCENDANTS = auto()

class Token:
    
    def __init__(self, token_type: TokenType, token_kind: TokenKind, value: any, symbol: Optional[Symbol] = None) -> None:
        self.token_type = token_type
        self.token_kind = token_kind
        self.value = value
        self.symbol = symbol


    def __repr__(self) -> str:
        return f"Token(Type={self.token_type}, Kind={self.token_kind}, value={self.value}, symbol={repr(self.symbol)})"
