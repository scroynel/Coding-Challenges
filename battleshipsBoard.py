'''

Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words,
they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), 
where k can be of any size. At least one horizontal or vertical cell separates between 
two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0

'''

def countBattleships(board):
    count = 0
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == "X" and (board[i-1][j] != "X" or i-1 < 0) and (board[i][j-1] != "X" or j-1 < 0):
                count += 1

    return count


print(countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print(countBattleships([["."]]))