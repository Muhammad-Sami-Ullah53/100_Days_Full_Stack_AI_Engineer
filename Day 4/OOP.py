class Student:
    def __init__(self,name,age,gmail): # is line me jo name age orr gmail he wo neechy objects sy aye ga orr phr ye is constructor me use hoga
        self.name=name
        self.age=age
        self.gmail=age
    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gmail: {self.gmail}")
    def change_gmail(self,gmail):
        self.gmail=gmail

# Now creating objects
user=Student('Ali',20,'samiullah@gmail')
user.show_profile()
user.change_gmail('mygmail@gmail.com')
user.show_profile()
        
        

class BankAccount:
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
user1=BankAccount("hamza",0)
user1.display()
user1.deposite(500)
user1.withdraw(100)
user1.display()