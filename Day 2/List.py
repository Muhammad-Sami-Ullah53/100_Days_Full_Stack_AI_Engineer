# List ko hm koi b data type ki tarah use krty hn jisme hm multiple values ko store kr skty hn
# [] is the symbol of list
# List ki valures jo index sy access krty hein
# List ki values ko hm change b kr skty hn

Students = ["Sami", "Ali", "Ahmed"]
RollNo = [1, 2, 3]

# agr list me koi value change krni ho to usko overwrite kr dety hein like this
Students[0] = "Samiullah"

# agr list me specific index ki value ko add krna ho jis sy pahly wli value change b na ho orr new 
# value us index pe add ho jaye to us k liye insert() method ka use krty hn

Students.insert(1, "Zubair") # is me 1 index pe Zubair ko insert kr diya
print(Students)

# agr list k last me koi value add krni ho to us k liye append() method ka use krty hn
Students.append("Hassan") # is me list k last me Hassan ko add kr diya
print(Students)

