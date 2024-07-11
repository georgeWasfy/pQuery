from Token import Token, TokenType
from typing import List

class Lexer:
    keywords = ['null', 'true', 'false', 'and', 'or', 'not', 'in']
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

    def back(self) -> str:
        char = self.src[self.cursor]
        self.cursor -= 1
        return char

    def peek(self, **kwargs) -> str:
        step = kwargs.get('step', None)
        return self.src[self.cursor] if step == None else self.src[self.cursor + step]

    def skip_white_space(self) -> None:
        c = self.peek()
        while (c == ' ' or c == '\t' or c == '\n'):
            if (c == '\n'):
                self.line += 1
                self.begining_of_line = self.cursor
            self.advance()
            c = self.peek()
        return
    def skip_comments(self) -> None:
        char = self.advance()
        while(char != '*'):
            char = self.advance()
        if(self.peek() == '/'):
            self.advance()
            return
        raise ValueError('Comment has no closing tag')
        

    def next_token(self):
        if (self.is_file_end()):
            return Token(TokenType.EOF, 'EOF')
        self.skip_white_space()
        char = self.advance()
        #match identifiers
        if (char.isalpha()):
            s = self.match_identifier()
            if (s in self.keywords):
                token = self.construct_keyword_token(s)
            else:
                token = Token(TokenType.IDENTIFIER, s)
            return token
        
        #match numbers
        if (char.isdigit()):
            s = self.match_digit()
            return Token(TokenType.NUMBER, s)
        
        #match strings
        if (char == '"'):
            s = self.match_string()
            return Token(TokenType.STRING, s)
        
        #skip comments
        if(char == '/' and self.peek() == '*'):
            self.advance()
            self.skip_comments()
            return

        # match range operator
        if (char == '.' and self.peek() == '.'):
            self.advance()
            return Token(TokenType.RANGE, '..')

        token = self.match_literal(char)

        return token

    def tokenize(self):
        while not self.is_file_end():
            next = self.next_token()
            if(next != None):
                self.tokens.append(next)
        return self.tokens

    def match_string(self):
        string_start_idx = self.cursor
        char = self.advance()
        while (char != '"'):
            char = self.advance()
        return self.src[string_start_idx: self.cursor - 1]

    def match_identifier(self):
        start_idx = self.cursor - 1
        next_char = self.peek()
        while (next_char.isalnum()):
            next_char = self.advance()
        return self.src[start_idx: self.cursor - 1]

    def construct_keyword_token(self, str):
        token = None
        match str:
            case'true':
                token = Token(TokenType.BOOLEAN, 'true')
            case'false':
                token = Token(TokenType.BOOLEAN, 'false')
            case'null':
                token = Token(TokenType.BOOLEAN, 'null')
            case'and':
                token = Token(TokenType.AND, 'and')
            case'or':
                token = Token(TokenType.OR, 'or')
            case'not':
                token = Token(TokenType.NOT, 'not')
            case'in':
                token = Token(TokenType.IN, 'in')
            case _:
                raise ValueError("Expected Keyword", str, "at line",
                                 self.line, "at col", self.cursor - self.begining_of_line)
        return token

    def match_digit(self):
        start_idx = self.cursor - 1
        char = self.advance()
        while (char.isdigit()):
            char = self.advance()

        if (char == '.'):
            next = self.peek()
            if (next == '.'):   
                if(self.cursor - start_idx > 1):
                    self.back() 
                return self.src[start_idx: self.cursor]

            if (not next.isdigit()):
                raise ValueError("Expected a number found", next, "at line",
                                 self.line, "at col", self.cursor - self.begining_of_line)
            char = self.advance()

        while (char.isdigit()):
            char = self.advance()
        if(self.cursor - start_idx > 1):
            self.back()        
        return self.src[start_idx: self.cursor]

    def match_literal(self, char):
        token = None
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
            case'+':
                token = Token(TokenType.ADDITION, '+')
            case'-':
                token = Token(TokenType.SUBTRACTION, '-')
            case'*':
                token = Token(TokenType.MULTIPLICATION, '*')
            case'/':
                token = Token(TokenType.DIVISION, '/')
            case'%':
                token = Token(TokenType.MODULO, '%')
            case'=':
                token = Token(TokenType.EQUAL, '=')
            case'!':
                next = self.peek()
                if (next == '='):
                    self.advance()
                    token = Token(TokenType.NOTEQUAL, '!=')
            case'<':
                next = self.peek()
                if (next == '='):
                    self.advance()
                    token = Token(TokenType.LEQ, '<=')
                else:
                    token = Token(TokenType.LE, '<')
            case'>':
                next = self.peek()
                if (next == '='):
                    self.advance()
                    token = Token(TokenType.GTQ, '>=')
                else:
                    token = Token(TokenType.GT, '>')
            case _:
                raise ValueError("Unexpected Token", char, "at line",
                                 self.line, "at col", self.cursor - self.begining_of_line)
        return token
