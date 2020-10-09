 #!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    #most_common(1) returns tuple of (most common value, count)
    #subtract it from array length to find how many you need to remove 
    return len(arr) - Counter(arr).most_common(1)[0][1]

    
    


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    # result = equalizeArray(arr)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    arr = [1,2,2,2,3,3,4,5,6]
    result = equalizeArray(arr)
    print(result)

