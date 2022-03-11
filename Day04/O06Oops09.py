
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary


emp1 = Employee("Jane", 25000)
emp2 = Employee("Jill", 30000)

print(emp1)
print(emp2)
print("-" * 40)

# addition
print("Addition :", emp1 + emp2)

# subtraction
print("Subtraction :", emp1 - emp2)

# Multiplication
print("Multiplication :", emp1 * emp2)

# division
print("Division :", emp1 / emp2)

# floor
print("Floor Division :", emp1 // emp2)