
# for loop
i = 0
for i in range(1, 11):
    print(i, end=" ")
print()

print(f"After :{i}")

i = 10
while(i > 0):
    print(i, end=" ")
    i -= 1          # i = i - 1
print()

print("-" * 40)

for i in range(1, 21):
    if i % 2 == 0:
        continue                # skip the iteration
    # if i > 15:
    #     break
    print(i, end=" ")
else:
    print("\nfor loop completed....")
print()


