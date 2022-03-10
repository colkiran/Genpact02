
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("tell the range"))
if nterms <= 0:
    print("please enter a positive integer")
else:
    print("fabb series:")
    for i in range(nterms):
        print(recur_fibo(i), end=" ")
print()
