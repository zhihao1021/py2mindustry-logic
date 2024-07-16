from typing import Optional


class HasName():
    _name: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def _before_get_name(self) -> None:
        raise NotImplementedError

    def generate(self) -> None:
        if self._name:
            return
        self._before_get_name()

    @property
    def name(self) -> str:
        if self._name:
            return self._name
        self._before_get_name()
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
