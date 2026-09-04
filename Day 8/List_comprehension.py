# List comprehension ko hm tb use krty hein jb hm list ko bht hi choti aur simple trha se create krna chahty hein

# Agr kisi list k hr element pe koi operation krna ho to hm list comprehension ka use kr skty hein
# hm list k hr element pe operation lgany k lyye loop use krty hein orr usy list me store krty hein
users = ["Ali", "Sara", "John"]
names = []
for user in users:
    names.append(user.upper())
print(names)
    
    # yehi kaam hm list comprehension k zariye b kr skty hein
# new_list = [expression for item in iterable if condition]   ye syntax he orr condition optional he
new_list=[user.upper() for user in users]
print(new_list)

numbers=[1,2,3,4,5]
squares=[num**2 for num in numbers]
print(squares)


# agr kisi database me sy active users ko nkalna ho to esy karein gy
users = [
    {"name": "Ali", "active": True},
    {"name": "Sara", "active": False},
    {"name": "John", "active": True}
]
active_users=[user for user in users if user['active']==True]   # ye hr user ko check kry ga agr to user active he to user active_users  wli list me daal dy ga
print(active_users)
# upr wli list comprehension user ka name b orr active he ya nai ye b active users me daaly gi


# agr hm srf activer users ka name chahte hein to esy karein gy
active_user_names=[user['name'] for user in users if user['active']==True]
print(active_user_names)



products = [
    {"name": "Laptop", "price": 100000},
    {"name": "Mouse", "price": 2000},
    {"name": "Keyboard", "price": 5000}
]

# Get name of products with price greater than 5000
expensive_products=[product['name'] for product in products if product['price']>5000]
print(expensive_products)