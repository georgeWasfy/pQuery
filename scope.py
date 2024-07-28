from Token import KEYWORDS, Token

# WIP: for now no scope support


class Scope:
    defined = {}

    def define(self, token: Token):
        if (self.defined.get(token.value, None) is not None):
            if (token.value in KEYWORDS):
                raise ValueError("This is a reserved keyword")
            raise ValueError("This variable is already defined")
        self.defined[token.value] = token
        # this.def [n.value] = n
        # n.reserved = false
        # n.nud = itself
        # n.led = null
        # n.std = null
        # n.lbp = 0
        # n.scope = scope
        # return n
