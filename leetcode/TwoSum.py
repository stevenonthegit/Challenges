# https://leetcode.com/problems/two-sum/

"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""
def twoSum(nums, target):
    cache = {}  # a cache is used to 'lookbehind' at the values we've already traversed
                # that lets us search the list in linear time

    for (i, v) in enumerate(nums):
        i2 = cache.get(target-v) # e.g. our target=9, and currently v=7. we search the cache 
                                    # for a value 9-7 = 2, which would be a match
        if i2 != None: 
            return [i2,i]
        else:
            cache[v] = i    #no dice, so add current value,index to the cache and keep moving

print(Solution.twoSum([2,7,11,15], 9))