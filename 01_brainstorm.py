cat = ["category", "Countries", "Cities"]
anslist = []

import random

for i in range(1):
    cat_number = random.randint(0,2)

if cat_number == 0:
    category = cat[0]
if cat_number == 1:
    category = cat[1]

if cat_number == 2:
    category = cat[2]


print("Put in 10 random inputs")

for i in range(10):
    userA = input()
    anslist.append(userA)

for i in anslist:
    print(i.center(60,' '))
































































