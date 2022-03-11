
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __len__(self):
        return len(self.name)

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val

emp1 = Employee("Sachin")

print([t for t in emp1])

print('-' * 40)
emp1.append("Python")

print([t for t in emp1])

x = emp1[3]                 # __getitem__
print(f"x :{x}")

emp1[2] = "Django"          # __setitem__
print([t for t in emp1])