
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account.....")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def deposit(self):
        print("Amount credited into the account.....")

    def getBalance(self):
        print("get savings balance......")

sav = Savings()
sav.deposit()
sav.getBalance()
