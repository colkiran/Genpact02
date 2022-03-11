
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Justin", 35000)
print(emp1)

emp2 = Employee("David", 40000)
print(emp2)

print("-" * 40)
# print(emp1 == emp2)             # comparison of addresses by default

if emp1 == emp2:
    print("{0} salary of {1} is equal to {2} salary of {3}".format(emp1.name, emp1.salary,
                                                                   emp2.name, emp2.salary))
else:
    print("{0} salary of {1} is NOT equal to {2} salary of {3}".format(emp1.name, emp1.salary,
                                                                   emp2.name, emp2.salary))
print("-" * 40)

if emp1 != emp2:
    print("{2} salary of {3} is NOT equal to {0} salary of {1}".format(emp1.name, emp1.salary,
                                                                   emp2.name, emp2.salary))
else:
    print("{2} salary of {3} is equal to {0} salary of {1}".format(emp1.name, emp1.salary,
                                                                       emp2.name, emp2.salary))
print("-" * 40)

if emp1 > emp2:
    print("emp1 is greater {}".format(emp1.salary))
else:
    print("emp2 is greater {}".format(emp2.salary))

if emp1 < emp2:
    print("emp1 salary {0} is less than emp2 salary {1}".format(emp1.salary, emp2.salary))
else:
    print("emp2 salary {0} is less than emp1 salary {1}".format(emp2.salary, emp1.salary))
