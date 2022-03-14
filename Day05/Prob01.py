
FL = open("C:\Training\PycharmProjects\Genpact02\Resource\EMP.csv", "r")

gen = {}
desig = []
dept = []
sal = 0
hrf = 0
for line in FL.readlines():
    # print(line)
    g = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]

    if g not in gen:
        gen[g] = 1
    else:
        gen[g] += 1

    if ds not in desig:
        desig.append(ds)

    if dp not in dept:
        dept.append(dp)

    sal += int(line.split(",")[5])

    if g == "f" and dp == "HR":
        hrf += 1

FL.close()

print(f"Gender      :{gen}")
print(f"Department  :{dept}")
print(f"Designation :{desig}")
print(f"Salary      :{sal}")
print(f"There are {hrf} Females from HR department")
