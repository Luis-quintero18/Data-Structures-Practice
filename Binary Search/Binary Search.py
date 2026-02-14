"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3
"""

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        # Calculate the midpoint
        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        
        elif target < nums[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


print(binary_search([-1,0,2,4,6,8], 4))
    
