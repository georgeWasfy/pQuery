
OPERATORS = {
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
class Symbol:
    id = None
    lbp = 0

    def __init__(self, parser, value=None) -> None:
        self.parser = parser
        self.value = value or self.id
        self.lbp = OPERATORS.get(self.value, 0)
        self.first = None
        self.second = None

    def nud(self):
        raise ValueError("Undefined Symbol", self.value)

    def led(self, left):
        raise ValueError("Missing operator.")

    def __repr__(self):
        return "<'%s'>" % self.value


class Literal(Symbol):

    def nud(self):
        return self


class Infix(Symbol):
    """Infix operator"""
    rightAssoc = False

    def led(self, left):
        self.first = left
        rbp = self.lbp - int(self.rightAssoc)
        self.second = self.parser.expression(rbp)
        return self

    def __repr__(self):
        return "<'%s'>(%s, %s)" % (
            self.value, repr(self.first), repr(self.second)
        )
