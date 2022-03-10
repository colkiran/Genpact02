
"""
any variable declared inside a function is a local variable and is not accessible
outside the function
"""


globX = 100
print(f"before globX :{globX}")

def fun(x):             # local variable
    y = 500             # local variable
    globX = 250         # local variable
    print(f"y :{y}")
    print(f"x :{x}")
    print(f"inside globX :{globX}")

fun(50)
print(f"after globX :{globX}")
# print(f"x :{x}")

