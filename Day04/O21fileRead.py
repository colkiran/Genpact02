
FL = open("data.txt", "r")
# st = FL.read(3500)

# st = FL.readline(8530)              # one line at a time
# print(st)
#
# print("*-" * 55)
# st = FL.readline()
# print(st)

# st = FL.readlines()                  # read all the lines and store it in a []
# # print(f"{st}")
# print(len(st))
# for line in st:
#     print(line)

st = FL.readlines(855)
print(st)

FL.close()