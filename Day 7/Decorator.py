# A decorator is a function that adds extra behavior to another function without changing the original function's code.

def login():
    print("User logged in")  # ab agr hm login function k start pe orr end pe kuch add krna chahty hein to usko hm khud sy function k start orr last pe nai likhein gy q k kbi kbi 10 function huye to itny zda hm nai likhein gy blky hr function me decorator use kr lein gy orr decorator me hm wo cheez likhein gy jo hm ny login function k start orr end pe add krni he


def logger(func):   # func me wo wla function jaye ga jis me hm decorator ko use kr rhy hein

    def wrapper():
        print("Starting login")

        func()

        print("login finished")

    return wrapper
  
def login():
    print("User logged in")
login = logger(login)   # isko hm @ use kr k b use kr skty hein


@logger   # is line ka mtlb k login function ko logger function me pass krdo orr logger function me jo wrapper function he wo login function k start orr end pe add ho jaye gy
def login():
    print("User logged in ")
login()