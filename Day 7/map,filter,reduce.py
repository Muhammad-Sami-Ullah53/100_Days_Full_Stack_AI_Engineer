    # MAP

# kisi list k hr element pe koi function lgany k lye hm map use krty hein 
# yehi same kaam hm list pe loop lga k b kr skty hein lkn wo thora lamba ho jata he is lye map() ko use krty hein

l=[1,2,3,4]
def cube(x):
    return x*x*x
new_list=map(cube,l)      # is line ka mtlb k "l" naam ki sari list k hr element pe cube ka function apply krdo orr 1 map return krdo map ko hm print nai kr skty is lye usko pahly list me convert kr dein gy phr print karein gy
print(list(new_list))     # yaha pe map ko list me convert kr k print kr dia he

# map k andr hm lambda funtion b pass kr skty hein

new_list2=list(map(lambda x:x*x*x, l))  # ye b same upr wla function hi kaam kry ga
print(new_list2)



# FILTER


# kisi list me sy specific values ko filter out krna ho to filter use krty hein orr jin values pe funciton ki value false hogi wo values list me sy nikal jaye gi

def filter_func(a):
    return a>=2

new_list3=list(filter(filter_func,l))    # yaha pe filter_func() ki bjaye lambda function b use kr skty hein
print(new_list3)

# upr waly part ko hm user build function ki bjaye lambda function b use kr skty hein
new_list4=list(filter(lambda x:x>=2,l))
print(new_list4)



# REDUCE

# reduce ko sb sy pahly import knra prrta he functools sy
# reduce ko hm tb use krty hein jb kisi list wgera ko reduce krna ho [1,2,3,4] ye list k sth agr hm 2 arguments dy dein gy to 2 2 kr k sari list reduce ho jaye gi

from functools import reduce
reduce_list=reduce(lambda x,y:x+y, l)
print(reduce_list)