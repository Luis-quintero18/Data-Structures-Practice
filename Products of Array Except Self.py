"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]
"""

def prod(nums):
    storage = [1] * len(nums)
    prefix = 1
    suffix = 1

    # Insert prefix amounts in the storage
    for i in range(len(nums)):
        storage[i] = prefix
        prefix *= nums[i]
    
    # Loop backward through the list to calculate the suffixes
    for j in range(len(nums) - 1, -1, -1):
        storage[j] *= suffix
        suffix *= nums[j]

    return storage
    
print(prod([1,2,4,6]))