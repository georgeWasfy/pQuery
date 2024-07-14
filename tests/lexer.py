import unittest

from lexer import Lexer


class TestLexer(unittest.TestCase):
    def test_multi_char_op(self):
        test_expr = "and or not in"
        expected = "[Token(Type=operator, Kind=and, value=and), Token(Type=operator, Kind=or, value=or), Token(Type=operator, Kind=not, value=not), Token(Type=operator, Kind=in, value=in)]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_literal_values(self):
        test_expr = "true false null"
        expected = "[Token(Type=value, Kind=boolean, value=True), Token(Type=value, Kind=boolean, value=False), Token(Type=value, Kind=null, value=None)]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_comments(self):
        test_expr = "/*and or not in*/"
        expected = "[]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_single_char_op(self):
        test_expr = "{[]}(.^,:+-*/%=!=<<=>>=)"
        expected = "[Token(Type=operator, Kind=left_brace, value={), Token(Type=operator, Kind=left_bracket, value=[), Token(Type=operator, Kind=right_bracket, value=]), Token(Type=operator, Kind=right_brace, value=}), Token(Type=operator, Kind=left_parenthesis, value=(), Token(Type=operator, Kind=dot, value=.), Token(Type=operator, Kind=caret, value=^), Token(Type=operator, Kind=comma, value=,), Token(Type=operator, Kind=colon, value=:), Token(Type=operator, Kind=plus, value=+), Token(Type=operator, Kind=hyphen, value=-), Token(Type=operator, Kind=asterisk, value=*), Token(Type=operator, Kind=forward_slash, value=/), Token(Type=operator, Kind=percentage, value=%), Token(Type=operator, Kind=equal, value==), Token(Type=operator, Kind=notequal, value=!=), Token(Type=operator, Kind=lt, value=<), Token(Type=operator, Kind=leq, value=<=), Token(Type=operator, Kind=gt, value=>), Token(Type=operator, Kind=geq, value=>=), Token(Type=operator, Kind=right_parenthesis, value=))]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_integers1(self):
        test_expr = "1"
        expected = "[Token(Type=number, Kind=number, value=1)]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_integers2(self):
        test_expr = "12"
        expected = "[Token(Type=number, Kind=number, value=12)]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_floats1(self):
        test_expr = "1.0   ,"
        expected = "[Token(Type=number, Kind=number, value=1.0), Token(Type=operator, Kind=comma, value=,)]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_floats2(self):
        test_expr = "12.44,"
        expected = "[Token(Type=number, Kind=number, value=12.44), Token(Type=operator, Kind=comma, value=,)]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_range_op(self):
        test_expr = "[1..3]"
        expected = "[Token(Type=operator, Kind=left_bracket, value=[), Token(Type=number, Kind=number, value=1), Token(Type=operator, Kind=range, value=..), Token(Type=number, Kind=number, value=3), Token(Type=operator, Kind=right_bracket, value=])]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_strings(self):
        test_expr = '"string1" "string2"'
        expected = "[Token(Type=string, Kind=string, value=string1), Token(Type=string, Kind=string, value=string2)]"
        lexer = Lexer(test_expr)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)
