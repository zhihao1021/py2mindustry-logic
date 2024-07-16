from typing import Any, Callable

from ..const import OperationCode
from ..swap import result
from ..utils import generateName
from ..variable import Comparation, Variable, variableType2Command

__if_group_data = {}
__for_group_data = {}
__goto_labels = []


class __Complex():
    __data: tuple
    __call: int = 0

    def __init__(
        self,
        *args,
        call: int = 0
    ) -> None:
        self.__data = args
        self.__call = call

    def __call__(self) -> Any:
        self.__data[self.__call]()

    def __iter__(self):
        return (f for f in self.__data)


def goto_statment() -> tuple[Callable[[], None], Callable[[], None]]:
    label_name = generateName()

    def goto():
        result.append(
            f"jump {label_name} always"
        )

    def label():
        if label_name in __goto_labels:
            raise RuntimeError("This label already exist.")

        result.append(
            f"{label_name}:"
        )
        __goto_labels.append(label_name)

    return goto, label


def if_else_statment(
    comparation: Comparation
) -> tuple[Callable[[], None], Callable[[], None], Callable[[], None]]:
    group_name = generateName()

    def if_func():
        if __if_group_data.get(group_name) == -1:
            raise RuntimeError("This if statment already close.")
        if __if_group_data.get(group_name):
            raise RuntimeError("This if statment already open.")

        if_tag = f"{group_name}_if"
        else_tag = f"{group_name}_else"
        oper = comparation.operator
        a = variableType2Command(comparation.a)
        b = variableType2Command(comparation.b)
        result.extend([
            f"jump {if_tag} {oper} {a} {b}",
            f"jump {else_tag} always",
            f"{if_tag}:"
        ])

        __if_group_data[group_name] = 0

    def else_func():
        if __if_group_data.get(group_name) is None:
            raise RuntimeError("This if-else statment not open yet.")
        if __if_group_data.get(group_name) == 1:
            raise RuntimeError("This else statment already open.")
        if __if_group_data.get(group_name) == -1:
            raise RuntimeError("This if-else statment already close.")

        else_tag = f"{group_name}_else"
        end_tag = f"{group_name}_fi"

        result.extend([
            f"jump {end_tag} always",
            f"{else_tag}:"
        ])

        __if_group_data[group_name] = 1

    def fi_func():
        if __if_group_data.get(group_name) == -1:
            raise RuntimeError("This if-else statment already close.")

        else_tag = f"{group_name}_else"
        end_tag = f"{group_name}_fi"

        if __if_group_data.get(group_name) == 0:
            result.extend([
                f"{else_tag}:"
            ])
        result.extend([
            f"{end_tag}:"
        ])

        __if_group_data[group_name] = -1

    return if_func, else_func, fi_func


def if_s(comparation: Comparation) -> __Complex:
    if_func, else_func, fi_func = if_else_statment(comparation=comparation)

    if_func()
    else_fi = __Complex(else_func, fi_func, call=1)

    return else_fi


def for_loop_statment(
    startValue: int = 0,
    stopValue: int = 0
) -> tuple[Callable[[], None], Callable[[], None], Variable]:
    group_name = generateName()
    i = Variable(name=f"{group_name}_i", value=startValue)

    def for_func():
        if __for_group_data.get(group_name) == -1:
            raise RuntimeError("This for statment already close.")
        if __for_group_data.get(group_name):
            raise RuntimeError("This for statment already open.")

        i.generate()

        start_tag = f"{group_name}_for"
        end_tag = f"{group_name}_rof"

        result.extend([
            f"{start_tag}:",
            f"jump {end_tag} {OperationCode.greaterThanEq} {i.name} {stopValue}",
        ])

        __for_group_data[group_name] = 0

    def rof_fouc():
        if __for_group_data.get(group_name) is None:
            raise RuntimeError("This for statment not open yet.")
        if __for_group_data.get(group_name) == -1:
            raise RuntimeError("This for statment already close.")

        start_tag = f"{group_name}_for"
        end_tag = f"{group_name}_rof"

        result.extend([
            f"op add {i.name} {i.name} 1",
            f"jump {start_tag} always",
            f"{end_tag}:"
        ])

        __for_group_data[group_name] = -1

    return for_func, rof_fouc, i


def for_s(
    startValue: int = 0,
    stopValue: int = 0
) -> tuple[Callable[[], None], Variable]:
    for_func, rof_func, variable = for_loop_statment(
        startValue=startValue,
        stopValue=stopValue
    )

    for_func()
    return __Complex(rof_func, variable, call=0)


def wait_statment(seconds: float):
    result.append(f"wait {seconds}")


def end_statment():
    result.append("end")


def stop_statment():
    result.append("stop")
