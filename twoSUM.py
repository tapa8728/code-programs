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
        ans = []
        #print type(nums)
        for each in nums:
            val = target-each
            if val in nums and val!=each:
                ans.append(nums.index(each))
                ans.append(nums.index(val))
                print ans
                break
            else:
                pass
        return ans

s = Solution()
print s.twoSum([0,3,2,4,0], 0)