from typing import Optional

from .const import PropertieCode, TargetCode
from .propertie import HasPropertie
from .swap import result
from .utils import generateName


class Unit(HasPropertie):
    _radar: Optional[HasPropertie] = None,
    _target: list[str] = [],
    _sort: Optional[str] = None,
    _max_or_nearest: bool = True,

    def __init__(
        self,
        radar: Optional[HasPropertie] = None,
        target: list[str] = [],
        sort: Optional[str] = None,
        max_or_nearest: bool = True,
    ) -> None:
        if radar is None:
            self._name = PropertieCode.unit
        else:
            self._radar = radar
            self._target = target
            self._sort = sort
            self._max_or_nearest = max_or_nearest

    def _before_get_name(self) -> None:
        self._name = generateName()

        target = " ".join((self._target + [TargetCode.any] * 3)[:3])
        order = 1 if self._max_or_nearest else 0

        if type(self._radar) == self.__class__:
            result.append(
                f"uradar {target} {self._sort} {order} {self._name}"
            )
        else:
            radar = self._radar.name
            result.append(
                f"uradar {target} {self._sort} {radar} {order} {self._name}"
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
