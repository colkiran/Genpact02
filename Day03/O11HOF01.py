
def add(x, y):
    print("add function called.....")
    return x + y

def sub(x, y):
    print("sub function called.....")
    return x - y

def multi(x, y):
    print("multi function called.....")
    return x * y

def outerFun(fnc):              # fnc is a variable
    def helperFun(*args):
        print("logged into the service.....")
        print(fnc(*args))
        print("logged out of the service......")
        print("-" * 40)

    return helperFun


addRef = outerFun(add)
addRef(15, 25)

subRef = outerFun(sub)
subRef(85, 30)

multiRef = outerFun(multi)
multiRef(10, 40)
