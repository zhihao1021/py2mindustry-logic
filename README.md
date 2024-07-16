# Py2mindustry logic generator
> A generator convert python code to mindustry logic

## How to use

First, write the python code.

Here is a example that make drone to transport phaseFabric from nucleus to projector:
```python
from py2logic import compile
from py2logic.building import Building
from py2logic.const import BuildingGroup, ItemCode, PropertieCode, UnitCode
from py2logic.function.flow_control import goto_statment, wait_statment, if_s
from py2logic.function.unit import (
    approach,
    bind_unit,
    check_inrange,
    take_item,
    drop_item,
    locate_building
)
from py2logic.unit import Unit


def main():
    loop, loop_label = goto_statment()
    wait_inrange, wait_inrange_label = goto_statment()
    wait_inrange2, wait_inrange_label2 = goto_statment()

    target = Building("projector1")

    bind_unit(UnitCode.poly)

    # ====== get nucleus info ======
    nuc_x, nuc_y, _, nucleus = locate_building(
        BuildingGroup.core,
        False
    )
    # ====== get nucleus info ======

    loop_label()

    # ====== goto nucleus ======
    approach(nuc_x, nuc_y, 3)

    wait_inrange_label()
    wait_statment(0.1)
    else_, fi_ = if_s(check_inrange(nuc_x, nuc_y, 4))
    else_()
    wait_inrange()
    fi_()
    # ====== goto nucleus ======

    # ====== take resource ======
    take_item(
        nucleus,
        ItemCode.phaseFabric,
        Unit().get(PropertieCode.itemCapacity),
    )
    # ====== take resource ======

    # ====== goto projector ======
    target_x = target.get(PropertieCode.x)
    target_y = target.get(PropertieCode.y)
    approach(target_x, target_y, 3)

    wait_inrange_label2()
    wait_statment(0.1)
    else_2, fi_2 = if_s(check_inrange(target_x, target_y, 4))
    else_2()
    wait_inrange2()
    fi_2()
    # ====== goto projector ======

    # ====== put into projector ======
    drop_item(
        target,
        Unit().get(PropertieCode.itemCapacity)
    )
    # ====== put into projector ======

    loop()

if __name__ == "__main__":
    main()

    # This functio will output mindustry code to file
    compile()
```

After you finishe your code, run it directly.

Don't forget to add the `compile()` in the bottom of your code.

It will auto generate a `.mlog` file, here is the code.
