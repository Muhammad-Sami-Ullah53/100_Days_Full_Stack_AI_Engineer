 # tuple  is just like list but its value can't be change
 # is me jo value 1 dfa store hogai wo hmesha k lye ho gai ab us k sth hm koi b panga nai kr skty
 # is ko create krny k lye hm () bracket use krty hein
 
 # Empty tuple 
single=() 
 
 #tuple with items
point=(2,3)
colors=('red','blue','green')
 
 # Single item tuple needs coma
single=(2,)
not_tuple=(2)  # ye tuple nai he srf 2 value ko bracket me likha he

# Acces tuple value
print(point[0])
print(point[-1])

#Slicing
print(colors[0:])
print(colors[::1])   # tuple ko seeda seeda print kr dy ga -> 1 show krta he k hm ny forward me print krna he 
print(colors[::-1])  # tuple ko reverse kr k print kr dy ga -> -1 show krta he k hm ny revese me print krna he
 
# Unpacking the tuple
x,y = point  # point naam sy jo tuple hoga us ki 1st value x me store ho jy gi orr 2nd value y me chali jaye gi
print(x,y)

#Multiple Assignment
a,b,c=(1,2,3)
d,e,f=4,5,6
print(a,b,c,d,e,f)

# Swap variables elegantly
x,y=y,x
print(x,y)