import unittest

from lexer import Lexer


class TestLexer(unittest.TestCase):
    def test_numbers(self):
        test_obj = '''{
                "singlenumber": 1,
                "multi1": 12,
                "multi2":  1222,
                "singlefloat": 1.0,
                "floatmulti": 11.555,
                }'''
        excepted = "[Token(Type=left_brace, literal={), Token(Type=string, literal=singlenumber), Token(Type=colon, literal=:), Token(Type=number, literal=1), Token(Type=comma, literal=,), Token(Type=string, literal=multi1), Token(Type=colon, literal=:), Token(Type=number, literal=12), Token(Type=comma, literal=,), Token(Type=string, literal=multi2), Token(Type=colon, literal=:), Token(Type=number, literal=1222), Token(Type=comma, literal=,), Token(Type=string, literal=singlefloat), Token(Type=colon, literal=:), Token(Type=number, literal=1.0), Token(Type=comma, literal=,), Token(Type=string, literal=floatmulti), Token(Type=colon, literal=:), Token(Type=number, literal=11.555), Token(Type=comma, literal=,), Token(Type=right_brace, literal=})]"
        lexer = Lexer(test_obj)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), excepted)

    def test_numbers_and_operators(self):
        test_obj = '''{
                "equal": 1+1 = 2,
                "NE": 1+1 != 3,
                "GT": 22 / 7 > 3,
                "LE": 22 / 7 < 3,
                "GTE": 22 / 7 >= 3,
                "LET": 22 / 7 <= 3,
                "in": "world" in ["hello", "world"],
                "float": 11.555,
                "integer": 1222222,
                "range":[1..5],
                "mult": 3 * 4
            }'''
        expected = "[Token(Type=left_brace, literal={), Token(Type=string, literal=equal), Token(Type=colon, literal=:), Token(Type=number, literal=1), Token(Type=addition, literal=+), Token(Type=number, literal=1), Token(Type=equal, literal==), Token(Type=number, literal=2), Token(Type=comma, literal=,), Token(Type=string, literal=NE), Token(Type=colon, literal=:), Token(Type=number, literal=1), Token(Type=addition, literal=+), Token(Type=number, literal=1), Token(Type=notequal, literal=!=), Token(Type=number, literal=3), Token(Type=comma, literal=,), Token(Type=string, literal=GT), Token(Type=colon, literal=:), Token(Type=number, literal=22), Token(Type=division, literal=/), Token(Type=number, literal=7), Token(Type=gt, literal=>), Token(Type=number, literal=3), Token(Type=comma, literal=,), Token(Type=string, literal=LE), Token(Type=colon, literal=:), Token(Type=number, literal=22), Token(Type=division, literal=/), Token(Type=number, literal=7), Token(Type=le, literal=<), Token(Type=number, literal=3), Token(Type=comma, literal=,), Token(Type=string, literal=GTE), Token(Type=colon, literal=:), Token(Type=number, literal=22), Token(Type=division, literal=/), Token(Type=number, literal=7), Token(Type=gtq, literal=>=), Token(Type=number, literal=3), Token(Type=comma, literal=,), Token(Type=string, literal=LET), Token(Type=colon, literal=:), Token(Type=number, literal=22), Token(Type=division, literal=/), Token(Type=number, literal=7), Token(Type=leq, literal=<=), Token(Type=number, literal=3), Token(Type=comma, literal=,), Token(Type=string, literal=in), Token(Type=colon, literal=:), Token(Type=string, literal=world), Token(Type=in, literal=in), Token(Type=left_bracket, literal=[), Token(Type=string, literal=hello), Token(Type=comma, literal=,), Token(Type=string, literal=world), Token(Type=right_bracket, literal=]), Token(Type=comma, literal=,), Token(Type=string, literal=float), Token(Type=colon, literal=:), Token(Type=number, literal=11.555), Token(Type=comma, literal=,), Token(Type=string, literal=integer), Token(Type=colon, literal=:), Token(Type=number, literal=1222222), Token(Type=comma, literal=,), Token(Type=string, literal=range), Token(Type=colon, literal=:), Token(Type=left_bracket, literal=[), Token(Type=number, literal=1), Token(Type=range, literal=..), Token(Type=number, literal=5), Token(Type=right_bracket, literal=]), Token(Type=comma, literal=,), Token(Type=string, literal=mult), Token(Type=colon, literal=:), Token(Type=number, literal=3), Token(Type=asterisk, literal=*), Token(Type=number, literal=4), Token(Type=right_brace, literal=})]"
        lexer = Lexer(test_obj)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)

    def test_identifiers_and_comments(self):
        test_obj = '''{
                "FirstName": "Fred",
                "LastName": "John",
                /* Long-winded expressions might need some explanation */
                "FullName": FirstName + LastName
                }'''
        expected = "[Token(Type=left_brace, literal={), Token(Type=string, literal=FirstName), Token(Type=colon, literal=:), Token(Type=string, literal=Fred), Token(Type=comma, literal=,), Token(Type=string, literal=LastName), Token(Type=colon, literal=:), Token(Type=string, literal=John), Token(Type=comma, literal=,), Token(Type=string, literal=FullName), Token(Type=colon, literal=:), Token(Type=identifier, literal=FirstName), Token(Type=addition, literal=+), Token(Type=identifier, literal=LastName), Token(Type=right_brace, literal=})]"
        lexer = Lexer(test_obj)
        tokens = lexer.tokenize()
        self.assertEqual(str(tokens), expected)
