from typing import List
from lexer import Lexer
from Token import Token
from symbol import Infix, Literal, Symbol


class Parser:
    current_token_idx = 0
    current_token: Token = None
    symbol_table = {}

    def __init__(self) -> None:
        self.make_symbol("+", Infix)
        self.make_symbol("number", Literal)
        self.make_symbol("<end>", Literal)
        
    def make_symbol(self, sid, symbol_class=Symbol):
        symbol_table = self.symbol_table
        sym = symbol_table[sid] = symbol_table.get(sid, type(
            symbol_class.__name__,
            (symbol_class,),
            {'id': sid}
        ))
        return sym

    def advance(self, value=None) -> Token | None:
        if value and value not in (self.current_token.symbol.value, self.current_token.symbol.id):
            raise ValueError(
                "Expected `%s'; got `%s' instead" % (value, self.current_token.symbol.value))

        if (self.current_token_idx >= len(self.tokens)):
            self.current_token = self.symbol_table["<end>"]
            return

        token = self.tokens[self.current_token_idx]
        self.current_token_idx += 1
        symbol_table = self.symbol_table
        # first look up symbol's value
        if token.value in symbol_table:
            sym = symbol_table[token.value]
        elif token.token_type in symbol_table:
            # then symbol's type
            sym = symbol_table[token.token_type]
        else:
            raise ValueError("Undefined token %s" % repr(token))

        self.token = token
        self.token.symbol = sym(self, token.value)
        return self.token

    def parse(self, source):
        lexer = Lexer(source)
        try:
            self.tokens = lexer.tokenize()
            self.advance()
            exp = self.expression(0)
            return exp
        finally:
            self.tokens = []
            self.token = None
            
    def expression(self, rbp):
        tok = self.token
        self.advance()
        left = tok.symbol.nud()
        while rbp < self.token.symbol.lbp:
            tok = self.token
            self.advance()
            left = tok.symbol.led(left)
        return left
