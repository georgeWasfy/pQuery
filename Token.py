from enum import auto, StrEnum


class TokenType(StrEnum):
    STRING = auto()
    NUMBER = auto()
    BOOLEAN = auto()
    NULL = auto()
    IDENTIFIER = auto()
    

    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()
    COLON = auto()
    EOF = auto()
    
class Token:
    def __init__(self, token_type: TokenType, literal: any) -> None:
        self.token_type = token_type
        self.literal = literal

    def __repr__(self) -> str:
        return f"Token(Type={self.token_type}, literal={self.literal})"
