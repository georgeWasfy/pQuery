
from types import NoneType
from typing import Union


JsonValue = Union["JsonObject", "JsonArray", str, int, float, bool, NoneType]
JsonObject = dict[str, JsonValue]
JsonArray = list[JsonValue]


def parse(input: str) -> JsonValue:
    pass
