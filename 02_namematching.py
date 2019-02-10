# First thing: get all lowercase
# First element of the array = uppercase. [0]
# Or just use a python function for it
from collections import defaultdict 

# What happens if no defaultdict? 
# Have to check if dictionary[key] is null? 
# If NULL, create a list
# append

with open("fall_users.txt") as f: # Opening the file
    line = f.readline()
    dictionary = defaultdict(list)
    reverse_dict = defaultdict(list)
    while line:
        res = line.rstrip().split("\t")
        rc1 = res[0].capitalize()
        rc2 = res[1].capitalize()
        # if dictionary[rc1] is NULL or reverse_dict[rc2] is NULL, make a list at those values. Only if no defaultdict
        dictionary[rc1].append(rc2)
        reverse_dict[rc2].append(rc1)
        line = f.readline()

# have key, value, and dictionary 
# What need is: First name(Followed by occurrence if > 1) : linked last names)
print("FIRST NAME(REPEATS) : LAST NAMES\n")
for k in dictionary: #for the key in dictionary
    v = dictionary[k] #value
    length = len(dictionary[k]) #length of the last names
    if length > 1: #checks whether the length of the last names array is greater than one
        print(k + "(" + str(length) + "):" + str(v))

print("\n\n")
# how many people share the input name + what last names are 
# how many people share input name + what first names are
# Have dictionary, key as firstname, value as lastname

#First name dicts, first name => [last name]
#Second name dicts, last name => [first]

print("LAST NAME(REPEATS) : FIRST NAMES\n")
for k in reverse_dict: #for the key in reverse dictionary
    v = reverse_dict[k] #value
    length = len(reverse_dict[k]) # the length of the first names array
    if(length > 1): #if the length is greater than one
        print(k + "(" + str(length) + "): " + str(v))

