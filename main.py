
from parser import Parser

numbers = '''{
    "singlenumber": 1,
    "multi1": 12,
    "multi2":  1222,
    "singlefloat": 1.0,
    "floatmulti": 11.555,
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
    parser = Parser()
    ast = parser.parse("1 + 1 + 1 + 1")
    print(ast)
