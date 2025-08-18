"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]
"""

# Create a function to encode the strings with length and delimeter
def encode(strs):
    return ''.join(f"{len(word)}#{word}" for word in strs)

def decode(s):
    starting_point = 0
    end_point = len(s)
    ans = []
    
    while starting_point < end_point:
        moving_point = starting_point
        # Check if the current character is the delimeter
        while s[moving_point] != "#":
            moving_point += 1
        word_length = int(s[starting_point:moving_point]) # This will be the length of the word we are looking for

        # Shift the index to avoid the delimeter
        moving_point += 1

        # Append the word to the list
        ans.append(s[moving_point:(moving_point+word_length)])

        starting_point = moving_point + word_length

    return ans

l = ["neet","code","love","you"]
encoded = encode(l)
print(encoded)
print(decode(encoded))