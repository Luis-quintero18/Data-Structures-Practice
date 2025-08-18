"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""

def valid_sudoku(board):
   # Create lists of sets to track what has been seen
   rows = [set() for _ in range(9)]
   cols = [set() for _ in range(9)]
   boxes = [set() for _ in range(9)]

    # Iterate over the board
   for row in range(9):
      for col in range(9):
        # Set the current square value of the board
        current_square = board[row][col]

        if current_square == ".":
           continue
        
        # The the box of the current square
        box = row // 3 * 3 + col // 3

        # Check if we have seen the current square value in any of the checked rows, cols, or boxes
        if current_square in rows[row] or current_square in cols[col] or current_square in boxes[box]:
           return False
        
        # Add the newly seen current square to the sets
        rows[row].add(current_square)
        cols[col].add(current_square)
        boxes[box].add(current_square)

   return True


board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(board))