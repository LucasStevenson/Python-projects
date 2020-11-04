#!/usr/bin/env python3

import sys
import math
import argparse
from prettytable import PrettyTable

# Setting up the parser and the -tags
parser = argparse.ArgumentParser()
parser.add_argument('-li', help="list of numbers separated by commas")
parser.add_argument('-sd', action='store_true',
                    help="display standard deviation table")
parser.add_argument('-pr', help="shows percentile rank. Needs raw score as argument.")
parser.add_argument('-bp', action='store_true', help="binomial probabilty")
args = parser.parse_args()


del sys.argv[0]  # this deletes the filename because i dont need that
if len(sys.argv) < 1 or (args.li == None and args.bp == False):  # neither li or bp was set
    print("You need to put in some sort of input. Use -h for more help")
    sys.exit()
elif args.li != None and args.bp: # li and binomial prob can't be in the same command
    print("-bp and -li should not be used in the same command")
    sys.exit()
elif args.bp:
    from fractions import Fraction
    # Binomial Probability

    def binomialProbability(n, x, p):
        # n = fixed number of trials
        # x = specified number of successes
        # p = probability of success on any given trial
        q = 1-p
        if n - x < 0 or n < 0 or x < 0:
            return "undefined"
        nCx = (math.factorial(n))/(math.factorial(x)*math.factorial(n-x))
        return Fraction(nCx * p**x * q**(n-x)).limit_denominator()

    try:
        n = float(sum(Fraction(s) for s in input("Fixed number of trials (n): ").split()))
        x = float(sum(Fraction(s) for s in input("Specified number of successes (x): ").split()))
        p = float(sum(Fraction(s) for s in input("Probability of success on any given trial (p): ").split()))
    except KeyboardInterrupt:
        sys.exit()

    print("\nBinomial Probability: " + str(binomialProbability(n, x, p)))
    sys.exit()

x = args.li.split(",")
nums = [float(i) for i in x]  # This converts strings in list into integers
ogNums = nums.copy()
nums.sort()
length = len(nums)


def minimum(nums):
    return(nums[0])


def maximum(nums):
    return(nums[-1])


def average(nums):
    total = 0
    for i in nums:
        total += i
    return(total/length)

# Make a copy of nums(So I don't change the original list)
# Iterate through while nums, then have conditional logic if length of list is 1 or 2
# If 1, return lst[0], if 2, list[0] + list[1] / 2
# del [0] and del [-1] to take out first and last elements of the list


def median(nums):
    new_list = nums.copy()
    while new_list:
        if len(new_list) == 1:
            return new_list[0]
        elif len(new_list) == 2:
            return((new_list[0] + new_list[1])/2)

        # How to reduce size of list?
        del new_list[0]
        del new_list[-1]

# Make a dictionary to count number of occurrences of each number, then choose the highest in values (O^N)


def mode(nums):
    dictionary = {}
    for i in nums:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    highest_occur = []
    occurs = -1  # the occurs is the number of times that it occurs
    for i in dictionary.keys():
        # if there is only one number that appears the most amt of times
        if dictionary[i] > occurs:
            occurs = dictionary[i]
            highest_occur = [i]
# if the number of occurences is the same
# Instead of a single value, make it a list
# If value is the same, add to list
# If value is less, ignore and move on

        # if there is either no number that appears more or there are more than one number
        elif dictionary[i] == occurs:
            highest_occur.append(i)
    return(highest_occur)

# dictionary[key which is the number] = value which is the number of times it occurred


def range(nums):
    return(maximum(nums) - minimum(nums))


def standardDeviation(nums):
    # SD Formula: SQRT((∑(Xi-µ)^2)/LENGTH)

    # First assign the ∑(Xi-µ)^2 to a variable (innerPart)
    # divide by length to get (∑(Xi-µ)^2)/LENGTH
    # return square root
    mu = average(nums)
    innerPart = 0
    for i in nums:
        # print((i-mu)**2)
        innerPart += (i-mu)**2
    innerPart /= length

    return math.sqrt(innerPart)


'''
Extra functions
'''
# Print out SD table

def standardDeviationTable(nums):
    mu = average(nums)
    t = PrettyTable(['x', 'µ', 'x-µ', '(x-µ)^2'])
    for i in nums:
        t.add_row([round(i, 3), round(mu, 3), round(i-mu, 3), round((i-mu)**2, 3)])
    return t

# Percentile rank

def percentileRank(nums):
    X = float(args.pr)
    belowX = 0
    equalX = 0
    for i in nums:
        if i < X:
            belowX += 1
        elif i == X:
            equalX += 1
    return ((belowX + (0.5 * equalX))/length) * 100


# When doing print, cast integers that are returned into strings because print likes strings and not ints
print("Min: " + str(minimum(nums)))
print("Max: " + str(maximum(nums)))
print("Average: " + str(average(nums)))
print("Median: " + str(median(nums)))
print("Mode: " + str(mode(nums)))
print("Range: " + str(range(nums)))
print("StandardDeviation: " + str(standardDeviation(nums)))

if args.sd:
    print(standardDeviationTable(ogNums))
if args.pr != None:
    print("Percentile Rank: " + str(percentileRank(nums)))
