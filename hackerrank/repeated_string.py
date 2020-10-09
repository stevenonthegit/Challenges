#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #s = the string fragment e.g "aba" or "aaca"
    #n = length of total string e.g. 10 or 678000
    #returns the number of "a" characters in the total string

    #multiplies count by whole integer quotient, then adds count from remainder substring
    return s.count('a') * n//len(s) + s[:n % len(s)].count('a')

    



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()

    #n = int(input())

    s = 'aba'
    n = 10

    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
