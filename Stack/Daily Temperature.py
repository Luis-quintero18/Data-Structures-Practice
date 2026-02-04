"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]
Output: [0,0,0]
"""
# solution [1, 0, 1, 0, 0, 0, 0]
# stack [1]
def dailyTemp(temperatures):
    solution = [0] * len(temperatures)
    # We can use a stack to track the indices
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            val = stack.pop()
            solution[val] = i - val
    
        stack.append(i)

    return solution

print(dailyTemp([22,21,20]))