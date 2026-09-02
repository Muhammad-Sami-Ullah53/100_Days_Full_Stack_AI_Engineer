# file=open('users.txt','r')  # hm is trha b file open kr skty hein lkn phr last me file ko close b krna prry ga 
# Lkn agr with open wly treeky  sy karein gy to file task perform kr k automatically close ho jaye gi

with open("users.txt", "w") as file:  # is me hmari file open hogi orr phr us me data write hoga orr jb data write ho jaye ga to file automatically close ho jaye gi
    data = file.write('This is file content')
    

with open("users.txt","r") as file:  # is me hmari file open hogi orr data read ho jaye ga jo b file me present hoga
    data=file.read()
    print(data)
    
# jb tk file close ho gi hm koi b operation perform nai kr skty jb b koi opertation perform krna he tb with open waly treeky sy file ko open kr lena he orr jo b file pe opertaion lgana he wo lga dena he

# with open('users.txt','w') as file:        # is sy pahly wla jo b data us me likha hoga wo dara dlt ho jaye ga orr new add ho jaye ga lkn hamy previous waly sy aagy hi add knra he to us k lye append ka method use karein gy
#     data=file.write("This is another content")
#     print(data)

with open("users.txt",'a') as file:
    data=file.write("\nThis is another content")
    
with open("users.txt","r") as file:
    data=file.read()
    print(data)