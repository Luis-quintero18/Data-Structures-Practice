"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true
"""

def valid_anagram(s, t):
    s_count = {}
    t_count = {}

    for char in s:
        s_count[char] = s_count.get(char, 0) + 1
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    if s_count == t_count:
        return True
    else:
        return False
    
s = "racecar"
t = "carrace"
u = "car"

print(valid_anagram(s, t))
print(valid_anagram(t, u))
