"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]
"""

def topk(nums, k):
    freq = {}

    # Create the Frequency Dictionary
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Create the Buckets
    n = len(nums)
    # We need 1 extra bucket than the length so the index matches the frequency
    buckets = [[] for i in range(n + 1)]

    # Fill the buckets with the corresponding dictionary keys
    for key in freq:
        buckets[freq[key]].append(key) # Example buckets[freq[1]].append(1)
    
    # Loop backwards through the buckets to get the most frequent items
    ans = []
    for bucket in range(n, 0, -1):
        for item in buckets[bucket]:
            ans.append(item)
            if len(ans) == k:
                return ans

nums = [1,2,2,2,3,3]          
print(topk(nums, 2))