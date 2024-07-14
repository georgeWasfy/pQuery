from enum import auto, StrEnum

class TokenType(StrEnum):
    VALUE = auto()  # ex: true, false, null
    NAME = auto()  # represents a key in json object
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    VARIABLE = auto()  # custom variable or pre-defined must start with $


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
    operators = {
        '.': 75,
        '[': 80,
        ']': 0,
        '{': 70,
        '}': 0,
        '(': 80,
        ')': 0,
        ',': 0,
        '@': 80,
        '#': 80,
        ';': 80,
        ':': 80,
        '?': 20,
        '+': 50,
        '-': 50,
        '*': 60,
        '/': 60,
        '%': 60,
        '|': 20,
        '=': 40,
        '<': 40,
        '>': 40,
        '^': 40,
        '**': 60,
        '..': 20,
        ':=': 10,
        '!=': 40,
        '<=': 40,
        '>=': 40,
        '~>': 40,
        'and': 30,
        'or': 25,
        'in': 40,
        '&': 50,
        '!': 0,  # not an operator, but needed as a stop character for name tokens
        '~': 0  # not an operator, but needed as a stop character for name tokens
    }

    def __init__(self, token_type: TokenType, token_kind: TokenKind, value: any) -> None:
        self.token_type = token_type
        self.token_kind = token_kind
        self.value = value

    def get_operator_precedence(self, operator):
        return self.operators.get(operator, None)

    def __repr__(self) -> str:
        return f"Token(Type={self.token_type}, Kind={self.token_kind}, value={self.value})"
