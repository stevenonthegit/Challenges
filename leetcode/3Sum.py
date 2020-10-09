# https://leetcode.com/problems/3sum/

"""
:type nums: List[int]
:rtype: List[List[int]]
"""
def threeSum(nums):
    ret = []
    nums.sort()

    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j]+ nums[k] == 0:
                    if [nums[i] , nums[j] , nums[k]] not in ret:
                        ret.append([nums[i] , nums[j] , nums[k]])
                
    return ret


print(threeSum([-1,0,1,2,-1,-4]))
        
        
    