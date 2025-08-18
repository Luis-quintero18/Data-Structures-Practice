"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""

def group_anagrams(strs):
    tracker = {}

    for word in strs:
        # Create a list to track the letters in a word
        letter_counter = [0] * 26

        # Increment the indexes of the list for the corresponding letters
        for char in word:
            letter_counter[ord(char) - ord('a')] += 1

        # Lists aren't hashable so convert it to a tuple to use as a key in the dictionary
        key = tuple(letter_counter)

        # Check is the letter counter list is in the dictionary. If it is append current word to the list if it's not initialize the list with the current word.
        if key in tracker:
            tracker[key].append(word)
        else:
            tracker[key] = [word]
        
    return list(tracker.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams(strs))