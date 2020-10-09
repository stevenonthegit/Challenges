#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    ar.sort()
    pairs = 0
    i = 0

    #for i in range(0, n-1):  
    ###can't use range as there is no way to increment "i" positional index conditionally
    while i < n-1:
        if ar[i] == ar[i+1]:
            pairs+=1
            i+=1
        i+=1

    return pairs

if __name__ == '__main__':
    
    n = 9
    ar = [10,20,20,10,10,30,50,10,20]
    print(sockMerchant(n, ar))

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #ar = list(map(int, input().rstrip().split()))

    #result = sockMerchant(n, ar)
    
    #fptr.write(str(result) + '\n')

    #fptr.close()
