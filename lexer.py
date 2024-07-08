from Token import Token, TokenType
from typing import List

class Lexer:
    tokens: List[Token]
    current_char = 0
    current_line = 1
    start_char = 0

    def __init__(self, src: str) -> None:
        self.src = src
        self.tokens = []

    def is_file_end(self):
        return self.current_char >= len(self.src)

    def advance(self) -> str:
        char = self.src[self.current_char]
        self.current_char += 1
        return char

    def peek(self) -> str:
        return self.src[self.current_char]

    def skip_white_space(self) -> None:
        c = self.peek()
        while (c == ' ' or c == '\t'):
            self.advance()
            c = self.peek()
        return

    def tokenize(self):
        while not self.is_file_end():
            self.skip_white_space()
            char = self.advance()
            match char:
                case'{':
                    self.tokens.append(Token(TokenType.LEFT_BRACE, '{'))
                case'}':
                    self.tokens.append(Token(TokenType.RIGHT_BRACE, '}'))
                case _:
                    print('Unrecognizable Chararcter')
    def get_tokens(self):
        return self.tokens
