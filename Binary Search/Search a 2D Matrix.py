"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""

def matrix_search(matrix, target):
    if not matrix or not matrix[0]:
            return False
        
    rows, cols = len(matrix), len(matrix[0])
    low = 0
    high = (rows * cols) - 1

    while low <= high:
        midpoint = (low + high) // 2
        row = midpoint // cols
        col = midpoint % cols

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            high = midpoint - 1
        else:
            low = midpoint + 1
    return False

print(matrix_search([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
