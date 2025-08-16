"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]
"""

def topk(nums, k):
    # Initialize a dictionary to store the frequencies of the numbers in the list
    freq = {}

    ans = []

    # Store the numbers as the key in a dictionary with their frequency as the value
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Create buckets for each frequency
    buckets = [[] for i in range(len(nums) + 1)]
    
    # Add the numbers to the appropriate bucket
    for num in freq:
        buckets[freq[num]].append(num)
        
    for i in range(len(buckets) - 1, 0, -1):
        for j in range(len(buckets[i]) - 1, -1, -1):
            ans.append(buckets[i][j])
            if len(ans) == k:
                return ans


nums = [1,2,2,3,3]
k= 2
print(topk(nums, k))