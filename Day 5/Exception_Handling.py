# try:
    # risky code

# except SomeException:
    # handle error

# else:
    # runs if no exception occurs

# finally:
    # always runs
 
try:
    age=int(input("Enter your age: "))
except ValueError:   #yaha pe koi exception du ya na du 1 hi baat he
    print("Invalid Input")
else:
    print("Your age has been recorded successfully")
finally:
    print("Program has been finished")
