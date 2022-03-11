
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):
    def doJob(self):
        print("Manager's Job.....")

class Developer(Employee):
    def doJob(self):
        print("Developer's Job.....")


def BankFun(emp):           # Polymorphism
    print("Bank Job Started".center(40, "-"))
    emp.doJob()
    print("Bank Job Completed".center(40, "-"))
    print("-" * 40)
    
Mike = Manager()
David = Developer()

BankFun(Mike)           # Managers Job
BankFun(David)          # Developers Job
