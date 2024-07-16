from typing import Literal, Optional, Union

from .base import HasName
from .const import OperationCode, PropertieCode
from .swap import result
from .utils import generateName

VariableType = Union[HasName, float, int, str]


def variableType2Command(variable: Optional[VariableType] = None) -> str:
    if variable is None:
        return PropertieCode.null
    return variable.name if issubclass(type(variable), HasName) else \
        f"\"{variable}\"" if type(variable) == str else \
        str(variable)


class VariableBase(HasName):
    def _comperator(operator: str):
        def wrapper(self: "VariableBase", value: VariableType) -> "Comparation":
            return Comparation(
                operator=operator,
                a=self,
                b=value
            )
        return lambda _: wrapper

    def _operator(
        operator: str,
        reverse: bool = False,
        override: bool = False,
    ):
        def wrapper(self: "VariableBase", value: Optional[VariableType] = None) -> "Operation":
            return Operation(
                operator=operator,
                a=value if reverse else self,
                b=self if reverse else value,
                override=override,
            )
        return lambda _: wrapper

    @_comperator(OperationCode.equal)
    def __eq__(self, value: VariableType) -> "Comparation": ...

    @_comperator(OperationCode.notEqual)
    def __ne__(self, value: VariableType) -> "Comparation": ...

    @_comperator(OperationCode.lessThan)
    def __lt__(self, value: VariableType) -> "Comparation": ...

    @_comperator(OperationCode.lessThanEq)
    def __le__(self, value: VariableType) -> "Comparation": ...

    @_comperator(OperationCode.greaterThan)
    def __gt__(self, value: VariableType) -> "Comparation": ...

    @_comperator(OperationCode.greaterThanEq)
    def __ge__(self, value: VariableType) -> "Comparation": ...

    @_comperator(OperationCode.strictEqual)
    def strictEqual(self, value: VariableType) -> "Comparation": ...

    @_operator(OperationCode.add)
    def __add__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.sub)
    def __sub__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.mul)
    def __mul__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.div)
    def __truediv__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.idiv)
    def __floordiv__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.mod)
    def __mod__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.pow)
    def __pow__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.shl)
    def __lshift__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.shr)
    def __rshift__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.or_)
    def __or__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.and_)
    def __and__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.xor)
    def __xor__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.add, reverse=True)
    def __radd__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.sub, reverse=True)
    def __rsub__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.mul, reverse=True)
    def __rmul__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.div, reverse=True)
    def __rtruediv__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.idiv, reverse=True)
    def __rfloordiv__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.mod, reverse=True)
    def __rmod__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.pow, reverse=True)
    def __rpow__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.shl, reverse=True)
    def __rlshift__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.shr, reverse=True)
    def __rrshift__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.or_, reverse=True)
    def __ror__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.and_, reverse=True)
    def __rand__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.xor, reverse=True)
    def __rxor__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.add, override=True)
    def __iadd__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.sub, override=True)
    def __isub__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.mul, override=True)
    def __imul__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.div, override=True)
    def __itruediv__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.idiv, override=True)
    def __ifloordiv__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.mod, override=True)
    def __imod__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.pow, override=True)
    def __ipow__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.shl, override=True)
    def __ilshift__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.shr, override=True)
    def __irshift__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.or_, override=True)
    def __ior__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.and_, override=True)
    def __iand__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.xor, override=True)
    def __ixor__(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.not_)
    def __invert__(self) -> "Operation": ...

    @_operator(OperationCode.abs)
    def __abs__(self) -> "Operation": ...

    @_operator(OperationCode.and_)
    def logicAnd(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.max)
    def max(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.min)
    def min(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.angle)
    def angle(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.len)
    def len(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.noise)
    def noise(self, value: VariableType) -> "Operation": ...

    @_operator(OperationCode.log)
    def log(self) -> "Operation": ...

    @_operator(OperationCode.log10)
    def log10(self) -> "Operation": ...

    @_operator(OperationCode.sin)
    def sin(self) -> "Operation": ...

    @_operator(OperationCode.cos)
    def cos(self) -> "Operation": ...

    @_operator(OperationCode.tan)
    def tan(self) -> "Operation": ...

    @_operator(OperationCode.floor)
    def floor(self) -> "Operation": ...

    @_operator(OperationCode.ceil)
    def ceil(self) -> "Operation": ...

    @_operator(OperationCode.sqrt)
    def sqrt(self) -> "Operation": ...

    @_operator(OperationCode.rand)
    def rand(self) -> "Operation": ...


class Variable(VariableBase):
    _name: str
    _value: VariableType

    def __init__(
        self,
        name: Optional[str] = generateName(),
        value: Optional[VariableType] = None
    ) -> None:
        if name:
            self._name = name
            if value:
                result.append(
                    f"set {self._name} {variableType2Command(value)}"
                )
        self._value = value or 0

    def _before_get_name(self) -> None:
        result.append(
            f"set {self._name} {variableType2Command(self._value)}"
        )


class Operation(VariableBase):
    _operator: str
    _a: VariableType
    _b: Optional[VariableType] = None

    def __init__(
        self,
        operator: str,
        a: VariableType,
        b: Optional[VariableType] = None,
        override: bool = False,
    ) -> None:
        self._operator = operator
        self._a = a
        self._b = b

        if override:
            self._name = a.name
            result.append(
                " ".join([
                    "op",
                    self._operator,
                    self._name,
                    variableType2Command(self._a),
                    variableType2Command(self._b)
                ])
            )

    def _before_get_name(self) -> None:
        self._name = generateName()
        result.append(
            " ".join([
                "op",
                self._operator,
                self._name,
                variableType2Command(self._a),
                variableType2Command(self._b)
            ])
        )


class Comparation(Operation):
    operator: Literal[
        "equal",
        "notEqual",
        "lessThan",
        "lessThanEq",
        "greaterThan",
        "greaterThanEq",
        "strictEqual",
    ]
    a: VariableType
    b: VariableType

    def __init__(
        self,
        operator: Literal[
            "equal",
            "notEqual",
            "lessThan",
            "lessThanEq",
            "greaterThan",
            "greaterThanEq",
            "strictEqual",
        ],
        a: VariableType,
        b: VariableType,
    ) -> None:
        super().__init__(
            operator=operator,
            a=a,
            b=b
        )
        self.operator = operator
        self.a = a
        self.b = b
