"""
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
"""

def lengthOfLongestSubstring(s):
    left = 0
    longest = 0
    seen = {}

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        longest = max(longest, right - left + 1)
    return longest

print(lengthOfLongestSubstring("zxyzxyz"))
    