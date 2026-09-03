
# jis function ko hm chahty hein k 1 line me bna dein orr 1 ya 2 dfa hi use ho srf to usy hn def k sth function nai bnaye gy blky lambda k sth bnaye gy
# lambda function ka koi naam nai hota ye srf 1 line me bna k use krne k lye hota he
# Syntax -> lambda arguments: expression 

double=lambda x:x*2
cube=lambda x:x*x*x
avg=lambda x,y:(x+y)/2

print(double(5))
print(cube(5))
print(avg(5, 10))

def cube(num):   #  isi function ko hm lambda function me convert kr skty hein
    return num*num*num
print(cube(5))

# upr wla function ko esy lambda me convert karein gy
cube = lambda num: num * num * num
print(cube(5))


# ab 1 value ko orr 1 function ko esy add karein kr skty hein
def addition(fun,value):
    return fun(value)+10

print(addition(lambda x: x * x * x, 2))