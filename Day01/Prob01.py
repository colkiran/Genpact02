
cntr = 0
for n in range (50, 150):
    count=0
    for i in range(2,(n//2+1)):
        if(n % i == 0):
            count = count + 1
            break
    else:
        print("%d" %n, end = "  ")
        cntr += 1
print()

print(f"There are {cntr} prime numbers between 150 and 50")
