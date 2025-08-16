"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
"""

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        # Calculate the complement number so we can check the dictionary for if we have seen it
        complement = target - nums[i]

        if complement in seen:
            # If the complement is in seen return a list of the indexes of the complement and the current loop index
            return [seen[complement], i]
        else:
            # If the complement is not seen store it in the dictionary
            seen[nums[i]] = i

# Test Cases
nums = [3,4,5,6]
print(two_sum(nums, 7))
print(two_sum(nums, 11))
print(two_sum(nums, 13))