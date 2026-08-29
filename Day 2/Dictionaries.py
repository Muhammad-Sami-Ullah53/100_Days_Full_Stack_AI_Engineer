# Dicitonaries me value ko store krny k lye us ka koi naam dena prrta he jisy key kahty hein
# is me key aur value dono ka use hota he
# key mtlb 1 naam orr value mtlb us key ki value
# Jb dictionayry bnani ho to {} ka use krty hn
# Jb dictionary ki koi value access krni ho to [] ka use krty hn orr us me key ka naam likhty hn

Student = {
    "name": "Sami",
    "rollno": 1,
    "dept": "Computer Science",
    "age": 20
}
print(Student["name"])

#kisi b specificvalue ko delete krna ho to del ka keyword use krty hn orr us me dictionary ka naam orr key ka naam likhty hn
del Student["rollno"]
print(Student)

#Remove and return
department = Student.pop("dept") # is me hm specific key ki value ko remove krty hn orr us value ko return b krwa skty hn 
# ab yaha pe dept me jo b value hogi wo remove ho jae gi orr us value ko department me store krwa diya jae ga
print(department)

#Add new key and value
Student["Subject"] = "Physics" # is me hm new key orr value ko add krty hn (ab agr yaha pe pahly sy subject hota to uski value change ho jani thi lkn yaha pahly sy subject nai tha new key add hogai subject k naam sy)

print(Student.values()) # is me hm sari values ko print krwa skty hn
print(Student.keys()) # is me hm sari keys ko print krwa skty hn
print(Student.items()) # is me hm sari keys orr values ko print krwa skty hn

# Check if key exist or not
if "age" in Student:
    print("Yes, 'age' is one of the keys in the Student dictionary.")
else:
    print("No, 'age' is not a key in the Student dictionary.")

#Update multiple values in dictionary
# multiple values ko 1 time pe change krny k lye update() method ka use krty hn
Student.update({"name": "Ali", "age": 21, "Subject": "Mathematics"})
print(Student)


# Nested Dictionaries        Ab is me hm 1 dictionary bnaye gy orr us dictionary k andr 1 key ki jo value likhni he wo value b 1 dictionary hi hogi
Students={
    'Sami': {'age':20, 'dept':'Computer Science'},
    'Hamza': {'age':21, 'dept':'Medical'}
}

# Access Nested dictionaries       Ab yaha pe hm bahr wli dictionary k sth 2 square brackets use karein gy pehli braces me inner dictionary ka naam jo k key b hogi orr dusri braces me usi dictionary ki key hogi 
print(Students['Sami']['dept'])    # Sami wli dictionary me jao  orr us k andr 
