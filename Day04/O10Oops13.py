
class Employee:

    def __init__(self):
        self.name = "Mike"
        self._dept = "HR"                   # protected varaible

    def disp_data(self):
        print(f"Name is {self.name} \nDepartment is {self._dept}")

emp1  = Employee()
emp1.disp_data()


print("-" * 40)

class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.name = "Manoj"
        self.dept = self._dept

    def disp_data(self):
        print(f"Name is {self.name} \nDepartment is {self._dept}")

mgr1 = Manager()
mgr1.disp_data()
