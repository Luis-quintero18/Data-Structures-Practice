"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
"""

def longest_consecutive(nums):
    if not nums:
        return 0
    
    tracker = set(nums)
    best_length = 0

    for num in tracker:
        if num - 1 not in tracker: # Makes sure we start at the beginning of a sequence
            starting_point = num
            sequence_length = 1

            while starting_point + 1 in tracker:
                starting_point += 1
                sequence_length += 1
            
            # Checks if we beat the previous best sequence length
            best_length = max(best_length, sequence_length)

    return best_length


print(longest_consecutive([2,20,4,10,3,4,5]))