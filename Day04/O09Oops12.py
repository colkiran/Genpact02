
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return "Name is :" + self.__name + " and tech is :" + ", ".join(v for v in self.tech)

emp1 = Employee("Jack")
print(emp1)
print("-" * 40)

print(emp1.__dict__)

# print(emp1.__name)
emp1._Employee__name = "Sameul"
print(emp1._Employee__name)

print("-" * 40)

print(emp1.__dict__)