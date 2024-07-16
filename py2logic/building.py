from typing import Optional, Union

from .const import OperationCode, PropertieCode
from .propertie import HasName, HasPropertie
from .swap import result
from .unit import Unit
from .utils import generateName
from .variable import VariableType, variableType2Command


class Building(HasPropertie):
    _index: Optional[int] = None

    def __init__(self, value: Union[str, int]) -> None:
        if type(value) == str:
            self._name = value
        elif type(value) == int:
            self._index = value

    def _before_get_name(self) -> None:
        if self._index:
            self._name = generateName()
            result.append(
                f"getlink {self._name} {self._index}"
            )
        else:
            raise RuntimeError("Unknow building.")

    def enable(self) -> None:
        stateVariable = generateName()
        endLabel = generateName()
        result.extend([
            f"sensor {stateVariable} {self.name} {PropertieCode.enabled}",
            f"jump {endLabel} {OperationCode.equal} {stateVariable} 1",
            f"control enabled {self.name} 1"
            f"{endLabel}:",
        ])

    def disable(self) -> None:
        stateVariable = generateName()
        endLabel = generateName()
        result.extend([
            f"sensor {stateVariable} {self.name} {PropertieCode.enabled}",
            f"jump {endLabel} {OperationCode.equal} {stateVariable} 0",
            f"control enabled {self.name} 0"
            f"{endLabel}:",
        ])

    def shoot(self, x: VariableType, y: VariableType) -> None:
        x = variableType2Command(x)
        y = variableType2Command(y)
        result.append(
            f"control shoot {self.name} {x} {y} 1"
        )

    def shootp(self, unit: HasName) -> None:
        result.append(
            f"control shoot {self.name} {unit.name} 1"
        )

    def stopShoot(self) -> None:
        result.append(
            f"control shoot {self.name} 0 0 0"
        )

    def config(self, value: VariableType) -> None:
        value = variableType2Command(value)
        result.append(
            f"control config {self.name} {value}"
        )

    def radar(
        self,
        target: list[str] = [],
        sort: Optional[str] = None,
        max_or_nearest: bool = True,
    ) -> "Unit":
        return Unit(
            radar=self,
            target=target,
            sort=sort,
            max_or_nearest=max_or_nearest
        )
