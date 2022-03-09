
from collections import namedtuple

nmdTpl = namedtuple("Employee", "ename dob desig salary")
emp = nmdTpl(ename="Micheal", dob="3/8/1985", desig="PL", salary=85000)

print(emp)
print("-" * 40)
print(f"Name        :{emp.ename}")
print(f"DOB         :{emp.dob}")
print(f"Designation :{emp.desig}")
print(f"Salary      :{emp.salary}")

# emp.ename = "Mike"
