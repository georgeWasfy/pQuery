from Token import Token, TokenType
from typing import List

class Lexer:
    tokens: List[Token]
    cursor = 0
    line = 1
    begining_of_line = 0

    def __init__(self, src: str) -> None:
        self.src = src
        self.tokens = []

    def is_file_end(self):
        return self.cursor >= len(self.src)

    def advance(self) -> str:
        char = self.src[self.cursor]
        self.cursor += 1
        return char

    def peek(self) -> str:
        return self.src[self.cursor]

    def skip_white_space(self) -> None:
        c = self.peek()
        while (c == ' ' or c == '\t'):
            self.advance()
            c = self.peek()
        return

    def next_token(self):
        if (self.is_file_end()):
            return Token(TokenType.EOF, 'EOF')
        token = None
        self.skip_white_space()
        char = self.advance()
        match char:
                case'{':
                    token = Token(TokenType.LEFT_BRACE, '{')
                case'}':
                    token = Token(TokenType.RIGHT_BRACE, '}')
                case'[':
                    token = Token(TokenType.LEFT_BRACKET, '[')
                case']':
                    token = Token(TokenType.RIGHT_BRACKET, ']')
                case',':
                    token = Token(TokenType.COMMA, ',')
                case':':
                    token = Token(TokenType.COLON, ':')
                case'\n':
                    self.line += 1
                    self.begining_of_line = self.cursor
                    token = Token(TokenType.NEW_LINE, '\n')
                case _:
                    raise ValueError("Unexpected Token", char, "at line",
                                     self.line, "at col", self.cursor - self.begining_of_line)

        return token

    def tokenize(self):
        while not self.is_file_end():
            next = self.next_token()
            self.tokens.append(next)
        return self.tokens
