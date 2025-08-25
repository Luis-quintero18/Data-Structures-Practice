"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
"""

def valid_palindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1          
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

print(valid_palindrome("Was it a car or a cat I saw?"))
print(valid_palindrome("Was it a car or a cat I saws?"))