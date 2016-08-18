'''
Given a sorted array, remove the duplicates in place such that each element appear 
only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.
'''

nums = [1,1,1]

n=len(nums)
count,curr=1,1
while count < n:
    if nums[curr]!=nums[curr-1]:
        curr+=1
    else:
        del nums[curr]
    count+=1

print len(nums)
print nums