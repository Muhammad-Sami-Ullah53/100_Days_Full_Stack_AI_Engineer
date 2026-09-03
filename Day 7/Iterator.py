# kisi list wgera ki 1 value ko at a time store krna ho to iterator ko use krty hein
# jb b iterator ki values ko access krna ho to next() ko use krty hein 

numbers = [10, 20, 30]
iterator = iter(numbers)  # iter() ko use kr k Iterator me numbers 1 order me store ho jaye gy hm unko next() sy at a time 1 number ko access kr skty hein
print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30