
# closure
def outerFun(info):
    inf = "Mr. " + info

    def innerFun():
        print(inf)

    return innerFun    # HOF - higher order function

outerFun("Sachin")()            # calls the innerFun

print("-" * 40)
print(outerFun.__name__)
print(outerFun("tendulkar").__name__)

print("-" * 40)
innerRef = outerFun("Rahul")
innerRef()                      # calls the innerFun