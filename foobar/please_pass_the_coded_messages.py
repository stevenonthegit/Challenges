#You have L, a list containing some digits (0 to 9). Write a function 
# answer(L) which finds the largest number that can be made from some 
# or all of these digits and is divisible by 3. If it is not possible 
# to make such a number, return 0 as the answer. L will contain anywhere 
# from 1 to 9 digits.  The same digit may appear multiple times in the 
# list, but each element in the list may only be used once.

from itertools import combinations

def answer(l):

    #split into items already divisible by 3 and those that are not
    #dividing them out here will avoid extra cycles later
    sumtotal3 = list(filter(lambda n: n%3==0, l))
    others = sorted(list(filter(lambda n: n%3, l)),reverse=True)
    
    #check all possible combinations in [others], from largest to smallest (one)
    #Because the list is sorted, and we are checking combinations, the first result where %3==0
    # is going to be the largest sum we can possibly find. 
    # More naive solutions will brute force the entire list. 
    found=False
    for r in range(len(others), 0, -1):
        for c in combinations(others, r):
            #when found a correct set, add it to the result and break out
            if sum(c) % 3 == 0:
                sumtotal3 += c
                break
        else:
            continue
        break
    
    return int(''.join(str(x) for x in sorted(sumtotal3,reverse=True))) if len(sumtotal3) else 0


if __name__ == '__main__':
    print(answer([4,0,3,6,2,1,7])) #expected 764310
    print(answer([3, 1, 4, 1])) #expected 4311
    print(answer([1,4])) #expected 0
