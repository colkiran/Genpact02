
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

res = factorial(5)
print(f"res :{res}")

"""
= 5 * fact(4)
= 5 * 4 * fact(4 - 1)
= 5 * 4 * 3 * fact(3 - 1)
= 5 * 4 * 3 * 2 * fact(1)
= 5 * 4 * 3 * 2 * 1
= 120
"""