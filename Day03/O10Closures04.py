
def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(name):
            import emojis
            emojised = emojis.encode(greet + " :" + sep + ": "  + name)
            print(emojised)
        return innerMostFun
    return innerFun


sepRef = outerFun("Welcome")
tiger = sepRef("tiger")
tiger("sheroff")

print("-" * 40)

lion = sepRef("lion")
lion("Sachin")



"""
outerFun("Welcome")("----->")("Sachin")

sepRef = outerFun("Hello")
nameRef = sepRef("====>")
nameRef("Sehwag")
"""