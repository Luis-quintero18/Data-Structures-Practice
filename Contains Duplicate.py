"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
Input: nums = [1, 2, 3, 3]

Output: true
"""

def contains_duplicates(nums):
    seen = {}

    for num in nums:
        if num in seen:
            return True
        else:
            seen[num] = 1
    return False

true_list = [1, 2, 3, 3]
false_list = [1, 2, 3, 4]

print(contains_duplicates(true_list))
print(contains_duplicates(false_list))