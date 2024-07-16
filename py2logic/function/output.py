from typing import Union

from ..building import Building
from ..swap import result
from ..variable import VariableType, variableType2Command

def println(value: VariableType):
    if type(value) == str:
        result.append(f"print \"{value}\n\"")
    else:
        result.append(f"print {variableType2Command(value)}")
        result.append(f"print \"\n\"")

def printlines(strings: list[str]):
    """
    String only!!!
    """
    string = "\n".join(strings)
    result.append(f"print \"{string}\n\"")

def print_flush(to: Union[str, Building]):
    if type(to) == str:
        result.append(f"printflush {to}")
    else:
        result.append(f"printflush {to.name}")
