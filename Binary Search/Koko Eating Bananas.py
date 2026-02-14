"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
"""

def koko(piles, h):
    low = 1
    high = max(piles)
    best = high

    while low <= high:
        mid = (low + high) // 2
        hours = 0

        for pile in piles:
            # Division that rounds up
            hours += (pile + mid - 1) // mid

        if hours <= h:
            best = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return best

print(koko([1,4,3,2], 9))
    
            


