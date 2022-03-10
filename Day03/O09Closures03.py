
def outerFun(greet):
    def innerFun(name):
        print(greet, name)

    return innerFun

outerFun("Welcome")("Sachin")           # calls the inner function
print('-' * 40)

#simple curry
#curry
enggrt = outerFun("Welcome")
hindigrt = outerFun("Namaskar")
tamilgrt = outerFun("Vanakam")
spanishgrt = outerFun("Hola")

#dish
hindigrt("Ravi")
tamilgrt("Dhoni")
spanishgrt("Messi")