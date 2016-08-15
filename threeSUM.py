'''
THREE SUM 
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        1 8 9 12 15 25
        """
        nums.sort()     #sorting the array in ascending order
        ans = []        #answer list
        
        for left in range(0, len(nums)-2):
            ## Define left, right, intr pointers
            intr = left+1     # 'intr' intermediate number
            right = len(nums)-1
            
            while intr<right and intr>left:     #'intr' should lie between left and right
                sum = nums[left] + nums[intr] + nums[right]
                if sum == 0: #match
                    ans.append([nums[left],nums[intr],nums[right]])
                    intr += 1   #to compare the next triplet within the same window
                elif sum > 0:
                    right -= 1
                elif sum < 0:
                    intr +=1 
        return list(set(map(tuple, ans)))

s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])