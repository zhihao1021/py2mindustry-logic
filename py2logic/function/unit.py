from typing import Optional, Union

from ..building import Building
from ..const import OperationCode, PropertieCode
from ..swap import result
from ..unit import Unit
from ..utils import generateName
from ..variable import (
    Comparation,
    Variable,
    VariableType,
    variableType2Command,
)


bind_stack: list[Union[Unit, str]] = []
has_unbind = False


def bind_unit(unit: Union[Unit, str]):
    global has_unbind

    bind_stack.append(unit)
    has_unbind = False
    result.append(
        f"ubind {unit.name if type(unit) == Unit else unit}"
    )


def unbind_unit():
    global has_unbind

    result.append("ucontrol unbind")
    has_unbind = True
    if bind_stack:
        bind_stack.pop()


def unbind_all():
    global has_unbind

    if not has_unbind:
        unbind_unit()

    for unit in bind_stack:
        result.extend([
            f"ubind {unit.name if type(unit) == Unit else unit}",
            "ucontrol unbind"
        ])
    bind_stack.clear()


def idle_unit():
    result.append("ucontrol idle")


def stop_unit():
    result.append("ucontrol stop")


def move(x: VariableType, y: VariableType):
    x = variableType2Command(x)
    y = variableType2Command(y)
    result.append(f"ucontrol move {x} {y}")


def approach(x: VariableType, y: VariableType, r: VariableType):
    x = variableType2Command(x)
    y = variableType2Command(y)
    r = variableType2Command(r)
    result.append(f"ucontrol approach {x} {y} {r}")


def path_find(x: VariableType, y: VariableType):
    x = variableType2Command(x)
    y = variableType2Command(y)
    result.append(f"ucontrol pathfind {x} {y}")


def auto_path_find():
    result.append("ucontrol autoPathfind")


def enable_boost():
    result.append("ucontrol boost 1")


def disable_boost():
    result.append("ucontrol boost 0")


def shoot_target(x: VariableType, y: VariableType):
    x = variableType2Command(x)
    y = variableType2Command(y)
    result.append(f"ucontrol target {x} {y} 1")


def shoot_target(unit: Unit):
    result.append(f"ucontrol targetp {unit.name} 1")


def stop_shoot():
    result.append("ucontrol target 0 0 0")


def drop_item(
    target: Building,
    num: Optional[VariableType] = None
):
    if num is None:
        num = Unit().get(PropertieCode.totalItems)
    num = variableType2Command(num)
    result.append(f"ucontrol itemDrop {target.name} {num}")


def take_item(
    target: Building,
    item: str,
    num: Optional[VariableType] = None
):
    if num is None:
        num = Unit().get(PropertieCode.itemCapacity)
    num = variableType2Command(num)
    result.append(f"ucontrol itemTake {target.name} {item} {num}")


def drop_payload():
    result.append("ucontrol payDrop")


def take_payload(unit: VariableType):
    result.append(f"ucontrol payTake {unit.strip('@')}")


def enter_payload_block():
    result.append("ucontrol payEnter")


def mine(x: VariableType, y: VariableType):
    x = variableType2Command(x)
    y = variableType2Command(y)
    result.append(f"ucontrol mine {x} {y}")


def flag_unit(value: VariableType):
    value = variableType2Command(value)
    result.append(f"ucontrol flag {value}")


def build(
    x: VariableType,
    y: VariableType,
    block: VariableType,
    rotation: VariableType,
    config: VariableType
):
    x = variableType2Command(x)
    y = variableType2Command(y)
    block = variableType2Command(block)
    rotation = variableType2Command(rotation)
    config = variableType2Command(config)
    result.append(
        f"ucontrol build {x} {y} {block} {rotation} {config}"
    )


def get_block(
    x: VariableType,
    y: VariableType,
) -> tuple[Variable, Variable, Variable]:
    x = variableType2Command(x)
    y = variableType2Command(y)

    group_name = generateName()
    type_name = f"{group_name}_type"
    building_name = f"{group_name}_building"
    floor_name = f"{group_name}floor"

    result.append(
        f"ucontrol getBlock {x} {y} {type_name} {building_name} {floor_name}"
    )

    return Variable(type_name), Variable(building_name), Variable(floor_name)


def check_inrange(
    x: VariableType,
    y: VariableType,
    r: VariableType,
) -> Variable:
    x = variableType2Command(x)
    y = variableType2Command(y)
    r = variableType2Command(r)

    inrange = generateName()

    result.append(
        f"ucontrol within {x} {y} {r} {inrange}"
    )

    return Comparation(OperationCode.equal, Variable(inrange), 1)


def locate_ore(
    ore: str
) -> tuple[Variable, Variable, Comparation]:
    group_name = generateName()

    x = f"{group_name}_x"
    y = f"{group_name}_y"
    found = f"{group_name}_found"

    result.append(
        f"ulocate ore core {ore} {x} {y} {found}"
    )

    return (
        Variable(x),
        Variable(y),
        Comparation(OperationCode.equal, Variable(found), 1),
    )


def locate_building(
    group: str,
    is_enemy: bool,
) -> tuple[Variable, Variable, Comparation, Building]:
    group_name = generateName()

    enemy = 1 if is_enemy else 0
    x = f"{group_name}_x"
    y = f"{group_name}_y"
    found = f"{group_name}_found"
    building = f"{group_name}_building"

    result.append(
        f"ulocate building {group} {enemy} null {x} {y} {found} {building}"
    )

    return (
        Variable(x),
        Variable(y),
        Comparation(OperationCode.equal, Variable(found), 1),
        Building(building),
    )


def locate_enemy_spawn() -> tuple[Variable, Variable, Comparation, Building]:
    group_name = generateName()

    x = f"{group_name}_x"
    y = f"{group_name}_y"
    found = f"{group_name}_found"
    building = f"{group_name}_building"

    result.append(
        f"ulocate spawn core 0 null {x} {y} {found} {building}"
    )

    return (
        Variable(x),
        Variable(y),
        Comparation(OperationCode.equal, Variable(found), 1),
        Building(building),
    )


def locate_friendly_damage() -> tuple[Variable, Variable, Comparation, Building]:
    group_name = generateName()

    x = f"{group_name}_x"
    y = f"{group_name}_y"
    found = f"{group_name}_found"
    building = f"{group_name}_building"

    result.append(
        f"ulocate damaged core 0 null {x} {y} {found} {building}"
    )

    return (
        Variable(x),
        Variable(y),
        Comparation(OperationCode.equal, Variable(found), 1),
        Building(building),
    )
