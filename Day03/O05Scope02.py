
globX = 100
print(f"before globX :{globX}")

def fun(x):         # local variable
    global globX
    globX += x
    print(f"Inside globX: {globX}")


fun(50)
print(f"after globX :{globX}")