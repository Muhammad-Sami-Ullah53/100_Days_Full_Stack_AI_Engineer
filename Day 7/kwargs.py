# **kwargs collect multiple named arguments and then convert into dictionary
def create_user(**kwargs):
    print(kwargs)
create_user(
    name='Sami', 
    gmail='msami@gamil.com', 
    country='Pakistan'
)

# Difference btw args and kwargs 
# *args collect positional arguments while *kwargs collect named arguments

# ye dono akthy b use ho skty hein
def create_request(*args, **kwargs):
    print("Positional arguments: ",args)
    print("Named arguments: ",kwargs)
create_request(
    "GET",
    "URL",
    name='Sami',
    gmail="msami@gmail.com"
) 