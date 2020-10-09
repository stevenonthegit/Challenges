#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    valleys = 0

    for step in s:
        #if flat plane and descending, our boy is entering a valley
        #note this does not count valley exits, only entrances. 
        #to count exists, just need a stack or bool to hold entrance/exists in memory. 
        if height == 0 and step == 'D':
            valleys += 1
        
        # U = +1, D = -1, adjust height accordingly
        height += 1 if step == 'U' else -1 
            
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
