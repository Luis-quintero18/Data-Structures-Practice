"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.
Note: This chart is known as a histogram.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8
"""

def lrih(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left_index = stack[-1] if stack else -1
            print(f"Left Index: {left_index}")
            width = i - left_index - 1
            print(f"width: {width}, i: {i}, ")
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

print(lrih([1,3,7]))