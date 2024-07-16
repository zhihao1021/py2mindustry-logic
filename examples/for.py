from py2logic import compile
from py2logic.function.flow_control import (
    for_loop_statment,
    for_s,
)
from py2logic.function.output import (
    println,
    print_flush
)

def main():
    # ====== for method 1 ======
    for1, rof1, i1 = for_loop_statment(0, 10)

    for1()      # start loop

    println(i1)  # use i

    rof1()      # close loop
    # ====== for method 1 ======
    
    # ====== for method 2, shorter ======
    rof2, i2 = for_s(0, 10) # start loop
    
    println(i2)             # use i

    rof2()                  # close loop
    # ====== for method 2 ======

    # ====== for method 3, shortest, omit i ======
    rof3 = for_s(0, 10) # start loop
    
    println("*")

    rof3()              # close loop
    # ====== for method 3 ======

    print_flush("message1")


if __name__ == "__main__":
    # Run your function
    main()

    # Output
    compile()
