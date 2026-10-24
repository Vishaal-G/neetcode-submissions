class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def solveHelper(row, col):
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return
            
            if board[row][col] == "X" or board[row][col] == "T":
                return 
            
            board[row][col] = "T"

            solveHelper(row + 1, col)
            solveHelper(row - 1, col)
            solveHelper(row, col + 1)
            solveHelper(row, col - 1)

        for row in range (len(board)):
            for col in range(len(board[0])):
                if ((row == 0 or col == 0 or row == len(board)-1 or col == len(board[0])-1) and board[row][col] == "O"):
                    solveHelper(row, col)
        
        for row in range(len(board)):
            for col in range (len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                
                if board[row][col] == "T":
                    board[row][col] = "O"
