
def outerFun():
    o_x = "greetings"
    print(f"Outside -1 :{o_x}")

    def innerFun():
        nonlocal o_x
        o_x = "Hi"
        print(f"o_x :{o_x}")
        print("Hello World....")

    innerFun()
    print(f"Outside -2 :{o_x}")

outerFun()


