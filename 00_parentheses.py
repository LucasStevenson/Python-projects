import sys

del sys.argv[0] # this deletes the file name because i dont need that
x = sys.argv # everything besides the file nam
y = " ".join(x)

vowels = ['A', 'E', 'I', 'O', 'U',]


def capitalize_every_other(string):
    new_string = ""
    counter = 0
    for i in (string):
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):


        # if the char is a letter
            # do counter % 2 check and add result to new string
            #add one to counter
        # if not a letter, print the thing and don't add to counter


            if counter % 2 == 0:
                new_string += i.lower()
            else:
                new_string += i.upper()
            counter += 1
        else:
            new_string += i
    return new_string
print(capitalize_every_other(y))



def UppVowelAst(string):
    a_new_string = ""
    s = (capitalize_every_other(string))

    for i in (s):
        if i in vowels:
            a_new_string += "*"
        else:
            a_new_string += i
    return a_new_string
print(UppVowelAst(y))


# Iterate through the entire string
# Count parentheses? Split left/right-- is there a point?
# Counter for left parentheses
# When will program be incorrect?
# More right paren than left paren = wrong instantly
# Right == left, if right > left at end, wrong
# Counter
# < 0, print out false then exit
# After running thru loop, if counter is > 0, print out false
# On right, plus one to counter. oN LEFT, minus one to counter
# The number of paren is 0. Cant be symetrical if num of paren is some other number


def check_parentheses(string):
    s = UppVowelAst(string)
    paren = 0 # i sure do love counters
    for i in s:
        if i == "(":
            paren += 1
        elif i == ")":
            paren -= 1
        if paren < 0:
            print("NOT BALANCED")
            return False
    if paren == 0:
        print("Balanced!")
    else:
        print("Not Balanced!")

check_parentheses(y)
