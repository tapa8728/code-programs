'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        while nums1 and nums2:
            if nums2[0] == nums1[0]:
                result.append(nums2.pop(0))
                nums1.pop(0)
            else:
                if nums2[0] > nums1[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
        return result         
        
s = Solution()
print s.intersect([1, 2, 2, 1], [2, 2]) #[2,2]
print s.intersect([1], [1,1,3]) #[1]