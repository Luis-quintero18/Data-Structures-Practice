"""
You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Input: height = [1,7,2,5,4,7,3,6]
Output: 36
"""

def water_containers(heights):
    l = 0
    r = len(heights) - 1
    max_water = 0

    while l < r:
        distance = r - l
        current_water = min(heights[l], heights[r]) * distance
        max_water = max(max_water, current_water)
        
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return max_water

print(water_containers([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))