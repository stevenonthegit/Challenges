#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    cur = 0
    while cur < len(c)-2:
        if c[cur+2] == 0:
            cur+=2
            jumps+=1
        else:
            cur+=1
            jumps+=1
    
    #need to make one final jump
    #loop terminated early to avoid indexoutofbounds
    if cur < len(c)-1:
        jumps+=1
    
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
