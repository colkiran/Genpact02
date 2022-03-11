

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __len__(self):
        return len(self.name)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Kevin", 45000)
print(emp1)

print("-" * 40)
print(len(emp1))

print("-" * 40)
print([t for t in emp1])

