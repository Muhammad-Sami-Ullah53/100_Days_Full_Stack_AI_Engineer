# try:
    # risky code

# except SomeException:
    # handle error

# else:
    # runs if no exception occurs

# finally:
    # always runs
    

#  backend me user sy age puchi jaa rhi ho to agr wo "twenty" is trha ki age likh dy to usy exception sy handle karein gy agr handle na kia to program crash kr jaye ga
 
try:
    age=int(input("Enter your age: "))
except ValueError:   #yaha pe koi exception du ya na du 1 hi baat he
    print("Invalid Input")
else:
    print("Your age has been recorded successfully")
finally:
    print("Program has been finished")


# Backend me database k errors ko b isi sy handle kia ja skta he

# Kbi kbi backend me apni marzi ki exception b create krni prrti he jis sy hm apny mutabiq condition lga skty hein

age=-5
if age<0:
    raise ValueError("Age cannot be negative")  #yaha pe hmne apni marzi ki exception create ki he


# custom Exception
class insufficientBalance(Exception):
    pass

account_balance=1000
withdraw_amount=1500
try:
    if withdraw_amount>account_balance:
        raise insufficientBalance("Insufficient Balance in your account")
except insufficientBalance as error:
    print(error)
