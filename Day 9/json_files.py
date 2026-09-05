# JSON = JavaScript Object Notation
# It is simply a text format for storing and sending data.
# JSON  orr python dictionary me bht similarities hein dono me key-value pair hota he orr dono me data ko store krty hein But:
# Python dictionary → Python object
# JSON → text/data format
# JSON me different functions hoty hein


# dumps()

# Used when you want to convert Python data into a JSON string.
import json

data={
    'name':'Sami',
    'age':20
}
json_data=json.dumps(data)  # Used when you want to convert Python data into a JSON string.
print(json_data)




# loads()

# Used when python recieves json data as a string and you want to convert it into a Python object.
json_data='{"my_name":"Sami", "my_age":20}'
python_data=json.loads(json_data)  # ye json k format me jo b data aya hoga usy python ki dictionary me convert kr dy ga
print(python_data)

print(type(python_data))
print(type(json_data))


# dump() -> ko tb b use krty hein jb hm data ko json files me store krty hein
import json

user = {
    "name": "Ali",
    "age": 21,
    "marks":[1,2,3,4,5]
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)        # yaha pe dump me 3 cheezein jaye gi
    # user -> jo data store krna he
    # file -> jis file me store krna he
    # indent=4 -> ye json ko readable bnany k lye use kia jata he
    
    
# load() -> ko files me sy data read krny k lye load() use krty hein
# import json

with open("user.json", "r") as file:
    user = json.load(file)
print(user['name'])
print(user['marks'][0])


# Industry Level example
with open("user.json","r") as new_file:
    new_data=json.load(new_file)
print(new_data["marks"])

print(type(new_data))