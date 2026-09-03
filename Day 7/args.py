# Usually function me hm parameters ko add(a,b) kr k pass krty hein lkn agr hamy pta hi na ho to k kitny number of arguments pass kr rhy hein to hm *args ka use krty hein

def add(*args):       # ab hm ny paramters me arguments ka tuple bna k pass kr dia he ab agr hm function me print(args) karein gy to wo tuple print ho jaye ga
    print(args)      
add(2,3,4,5) 

# agr hm sb arguments ko add krna chahty hein to us tuple pe loop lga k add kr lein gy
def add(*args):
    total=0
    for num in args:
        total+=num
    print(total)
add(1,2,3)