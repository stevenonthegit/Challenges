### https://www.hackerrank.com/challenges/new-year-chaos/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q = [x-1 for x in q] #adjustment positions to match indexes
    total_trades = 0
    for i in range(len(q)):
        # trades = q[i] - i
        if q[i] - i > 2:
            print("Too chaotic")
            return

        for j in range(max(q[i]-1,0),i):
            total_trades += 1 if q[j] > q[i] else 0

    print(total_trades)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
