#print number from 0 to 5
for i in range(6):
    print(i)
    
#print number from 1 to 5
for i in range(1,6):
    print(i)
    
#print number from 1 to 10 with a jump of 2
for i in range(1,10,2):    # is me pehla number staring point btaye ga 2nd number ending point btaye ga but ending point add nai hoga orr last wla number jump btaye k kinty ka jump lena he
    print(i)
    
#Loop through text
word="Sami"
for letter in word:
    print(letter)
    
#Loop through text with specific indexing
word="Sami"
for letter in word[0:3]:
    print(letter)

# Loop through text but reverse text     
word="ali"
for letter in word[::-1]:
    print(letter)
    
# Loop through list 
students=["ali","sami","hamza"]
for name in students:
    print(name) 
    
# Loop through list but reverse
students=["ali","sami","hamza"]
for name in students[::-1]:
    print(name)
    
# print active users and count active usersd
users = [
    {"name": "Ali", "active": True},
    {"name": "Sami", "active": False},
    {"name": "Ahmed", "active": True}
]
for user in users:
    if(user['active']):
        print(user['name'])