# Sets are the collection of unique values, they remove duplicates automatically
# Set ko create krny k 2 ways hein set() method orr {} braces
# Jb set() ka use karein gy to set me jo values rakhni he un sbki list bna k set() me put kr deni he
# sets unordered hoty hein

# Creating empty set
empty_set=set()

# Creating set with values
numbers={1,2,3,4}  # {} braces ka use kr k
fruits=set(['Apple','Mango','Banana'])
print(numbers)
print(fruits)

# Remove duplicates from a list
scores=[90,40,60,20,40,70]  # ye 1 list bnai he jis me duplicates b exist kr rhy hein
unique_scores=set(scores)   # ye duplicates ko remove kr k 1 new set me store kr dy ga jiska naam he unique_scores

# Remove duplicates from a list and store in another list
numbers=[40,48,45,46,48]
unique_numbers=list(set(numbers))
print(unique_numbers)

# Add items
fruits.add('Orange')
print(fruits)

#Remove items
# fruits.remove('Banana')  # error if not found
fruits.remove('Banana')  # No error if not found
print(fruits)

# check membeship
if 'Orange' in fruits:
    print("Orange is in fruits set")