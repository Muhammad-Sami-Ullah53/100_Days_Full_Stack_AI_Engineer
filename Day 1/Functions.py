
#  User defined functions ki explaination
# 1) sb sy pahly def keyword ka use kr k function define krty hn
# 2) us k baad function ka name likhty hn
# 3) us k baad parentheses () ka use krty hn
# 4) function ke andar ka code likhty hn

# Paramenters orr arguments ki explaination
# kuch functions ko input ki zarurat hoti hai jise hum parameters kehte hain
# jb functions call krty hn to hum un parameters ko values provide krty hn jise arguments kehte hain
  
  
#   Code
 
# Without parameters or arguments
def greet():
    print("Hello world")
    print("I am Sami")
greet()

# With parameters or arguments
def greet(name):
    print("Hello world")
    print(f"I am {name}")
greet("Sami")

# With by default arguments
# ab is me agr me koi b argument provide na krun to by default wali wali value use hogi jo me function define krty time likh di hogi
def greet(name="Sami"):
    print("Hello world")
    print(f"I am {name}")
greet()


# Function that return values as a result case 1
def increment(num,by):
    return num + by
result = increment(5,2)
print(f"Result: {result}")

# Function that return values as a result case 2
def increment2(num,by):
    return num + by
print(f"Result: {increment2(5,1)}")

#Argument with key value pairs
# is me hm argument me dictionary pass kr dein gy orr parameter me 1 variable pass kr dein gy jis me 
# wo sari dictionary store hogi
# is me hm parameter k sth double starik b lgaye gy means **
def save_user(**user):
    print(user)
save_user(id=1, name="Sami", dept="Computer Science")

#previous wly me sy hm dictionary ki koi specific value ko b print krwa skty hein like this
def save_user(**user):
    print(user['name'])
save_user(id=1, name="Sami", dept="Computer Science")    