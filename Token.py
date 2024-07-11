from enum import auto, StrEnum


class TokenType(StrEnum):
    STRING = auto()
    NUMBER = auto()
    BOOLEAN = auto()
    NULL = auto()
    IDENTIFIER = auto()
    
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
    # BACKTICK = auto()
    EOF = auto()
    
    # Arithmetic Operators
    ADDITION = auto()
    SUBTRACTION = auto()
    DIVISION = auto()
    RANGE = auto()

    # Comparison Operators
    EQUAL = auto()
    NOTEQUAL = auto()
    LE = auto()
    GT = auto()
    LEQ = auto()
    GTQ = auto()
    IN = auto()

    # Logical Operators
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # Path Operators
    MAP = auto()
    CARET = auto()
    DESCENDANTS = auto()

class Token:
    def __init__(self, token_type: TokenType, literal: any) -> None:
        self.token_type = token_type
        self.literal = literal

    def __repr__(self) -> str:
        return f"Token(Type={self.token_type}, literal={self.literal})"
