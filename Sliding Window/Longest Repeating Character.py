"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4

Example 2:
Input: s = "AAABABB", k = 1
Output: 5
"""

def characterReplacement(s, k):
    count = {}
    left = 0
    max_count = 0
    best = 0

    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        max_count = max(max_count, count[char])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best

print(characterReplacement("AAABABB", 1))
