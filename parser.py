from typing import List, Optional
from Token import Token, TokenType
from symbol import Symbol


class Parser:
    symbol_table = {}
    scope = {}
    current_token = None
    current_token_idx = 0

    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens

    def create_symbol(self, id: str, bp: Optional[int] = 0) -> Symbol:
        symbol = self.symbol_table.get(id, None)
        if (symbol):
            if (bp >= symbol['lbp']):
                symbol['lbp'] = bp
            return symbol
        symbol = Symbol(id, bp)
        self.symbol_table[id] = symbol
        return symbol

    def advance(self, id: Optional[str] = None) -> Symbol:
        if (id is not None and self.current_token['id'] != id):
            raise ValueError("Expected ", id)

        if (self.current_token_idx >= len(self.tokens)):
            self.current_token = Token(TokenType.EOF, 'eof')
            return
        token = self.tokens[self.current_token_idx]
        self.current_token_idx += 1
        value = token.value
        arity = token.token_type
        symbol = None
        if (arity == TokenType.IDENTIFIER):
            symbol = self.scope.get(value)
            
        if (arity == TokenType.STRING or arity == TokenType.NUMBER):
            arity = TokenType.LITERAL
            symbol = self.symbol_table[TokenType.LITERAL]
            
        # this must be an operator
        else:
            symbol = self.symbol_table.get(value, None)
            if (not symbol):
                raise ValueError('Unkown operator ', value)
            
        return Token(token.token_type, value, arity, symbol)
