
class BackAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(amount<self.balance):
            self.balance-=amount
        else:
            print("Insufficient Balance")
    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")