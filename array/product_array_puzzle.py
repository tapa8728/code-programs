'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

'''


def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    outlist = []    #output array
    n = len(nums)
    # go left to right : construct the left array 
    temp = 1
    for i in range(n):
        outlist.append(temp)
        temp = temp*nums[i]
        
    # go right to left : construct the right array
    temp = 1
    for i in range(n-1, -1, -1):
        outlist[i] = outlist[i]*temp
        temp = temp * nums[i]
        
    return outlist