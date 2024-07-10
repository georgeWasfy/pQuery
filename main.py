
from lexer import Lexer

empty = '''{
  "FirstName": "Fred",
  "s": action1,
  "int":  1,
  "float": 11.555,
  "zds": 1222222,
  "range":[1..5],
  "plus": 1 + 3,
  "divid":  1 / 3
  /* Long-winded expressions might need some explanation */
  }'''
logical = '''{
    "equal": 1+1 = 2,
    "NE": 1+1 != 3,
    "GT": 22 / 7 > 3,
    "LE": 22 / 7 < 3,
    "GTE": 22 / 7 >= 3,
    "LET": 22 / 7 <= 3,
    "in": "world" in ["hello", "world"]
  }'''
example_json = '''{
  "FirstName": "Fred",
  "Surname": "Smith",
  "Age": 28,
  "Address": {
    "Street": "Hursley Park",
    "City": "Winchester",
    "Postcode": "SO21 2JN"
  },
  "Phone": [
    {
      "type": "home",
      "number": "0203 544 1234"
    },
    {
      "type": "office",
      "number": "01962 001234"
    },
    {
      "type": "office",
      "number": "01962 001235"
    },
    {
      "type": "mobile",
      "number": "077 7700 1234"
    }
  ],
  "Email": [
    {
      "type": "office",
      "address": [
        "fred.smith@my-work.com",
        "fsmith@my-work.com"
      ]
    },
    {
      "type": "home",
      "address": [
        "freddy@my-social.com",
        "frederic.smith@very-serious.com"
      ]
    }
  ],
  "Other": {
    "Over 18 ?": true,
    "Misc": null,
    "Alternative.Address": {
      "Street": "Brick Lane",
      "City": "London",
      "Postcode": "E1 6RF"
    }
  }
}'''


if __name__ == "__main__":
    lexer = Lexer(logical)
    tokens = lexer.tokenize()
    print(tokens)
