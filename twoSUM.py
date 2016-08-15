'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i   


'''  dictionry: store the difference of element with target as the key
9-2 =   7   0
9-11 = -2   2
9-15 = -6   3

'''
s = Solution()
print s.twoSum([2, 7, 11, 15], 9)