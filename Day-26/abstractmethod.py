# Abstarction --> Hiding the complexity
from abc import ABC, abstractmethod
class bankAccount(ABC):
    def UserInfo(self):
        print("You can access user Information")
    def transactions(self):
        print("You can access user transactions")
    def History(self):
        print("You can access user History")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class saving(bankAccount):
    def deposit(self):
        print("Depositing to Saving Bank")
    def withdraw(self):
        print("WithDrawing from Saving Bank")
class FixedAccount(bankAccount):
    def deposit(self):
        print("Depositing to FixedAccount")
    def withdraw(self):
        print("WithDrawing from FixedAccount")
class current(bankAccount):
    def deposit(self):
        print("Depositing to current Bank")
    def withdraw(self):
        print("WithDrawing from current Bank")
class Domastic(bankAccount):
    def deposit(self):
        print("Depositing to Domastic account")
    def withdraw(self):
        print("WithDrawing from Domastic accounts")

print("--------------Saving Account---------------")
r = saving()
r.deposit()
r.withdraw()
r.UserInfo()
r.transactions()
r.History()
print("--------------Current Account---------------")
v2 = current()
v2.deposit()
v2.withdraw()
v2.UserInfo()
v2.transactions()
v2.History()
print("--------------Fixed Account---------------")
v3 = FixedAccount()
v3.deposit()
v3.withdraw()
v3.UserInfo()
v3.transactions()
v3.History()


