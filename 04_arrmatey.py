import sys

x = sys.argv

for i in range(len(x)):
    print("Argv of " + str(i) + " is " + str(x[i]))

lengthSorted = sorted(x, reverse = True, key = len)

for i in lengthSorted:
    print(i)
