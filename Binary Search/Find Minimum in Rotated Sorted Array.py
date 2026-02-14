"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

[4,5,6,7]

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0
"""

def rsa(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        right = nums[mid + 1] if mid != len(nums) - 1 else nums[0]
        left = nums[mid - 1] if mid != 0 else nums[-1]

        if nums[mid] < left:
            return nums[mid]
        if nums[mid] > right:
            return right
        
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid - 1

print(rsa([5, 1, 2, 3, 4]))
            

