
# closure
def outerFun(info):
    inf = "Mr. " + info

    def innerFun():
        print(inf)

    innerFun()

outerFun("Sachin")
