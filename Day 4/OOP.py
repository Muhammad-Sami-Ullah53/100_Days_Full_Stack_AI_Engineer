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
        
        

        