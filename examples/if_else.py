from py2logic import compile
from py2logic.const import PropertieCode, ItemCode
from py2logic.building import Building
from py2logic.function.flow_control import (
    if_else_statment,
    if_s,
)
from py2logic.function.output import (
    println,
    print_flush
)


def main():

    container1 = Building("container1")

    copper = container1.get(ItemCode.copper) / \
        container1.get(PropertieCode.itemCapacity)

    # ====== if-else method 1 ======
    if1, else1, fi1 = if_else_statment(
        copper > 0.5
    )

    if1()           # if
    println("123")

    else1()         # else (else block is omissible)
    println("456")

    fi1()           # close block
    # ====== if-else method 1 ======

    # ====== if-else method 2, shorter ======
    else2, fi2 = if_s(copper > 0.5)  # if
    println("123")

    else2()                         # else
    println("456")

    fi2()                           # close block
    # ====== if-else method 2 ======

    # ====== if-else method 3, shortest, omit else ======
    fi3 = if_s(copper > 0.5)    # if
    println("123")

    fi3()                       # close block
    # ====== if-else method 3 ======

    print_flush("message1")


if __name__ == "__main__":
    # Run your function
    main()

    # Output
    compile()
