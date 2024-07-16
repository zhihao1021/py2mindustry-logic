from typing import Optional

from .base import HasName
from .swap import result
from .utils import generateName
from .variable import VariableBase


class HasPropertie(HasName):
    def get(self, propertieName: str) -> "Propertie":
        return Propertie(
            self,
            propertieName
        )


class Propertie(VariableBase):
    _owner: HasPropertie
    _propertieName: str

    def __init__(
        self,
        owner: HasPropertie,
        propertieName: str,
    ):
        self._owner = owner
        self._propertieName = propertieName

    def _before_get_name(self) -> None:
        self._name = generateName()
        result.append(
            f"sensor {self._name} {self._owner.name} {self._propertieName}"
        )
