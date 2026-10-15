class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def existHelper(right, i, j):
            if right == len(word):
                return True
            if i >= len(board) or i < 0 or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[right]:
                return False
            
            board[i][j] = "#"
           
            found = existHelper(right +1, i+1, j) or existHelper(right +1, i-1, j) or existHelper(right + 1, i, j+1) or existHelper(right + 1, i, j-1)
        
            board[i][j] = word[right]

            return found
        

        for row in range (len(board)):
            for col in range (len(board[0])): 
                    if existHelper(0,row,col):
                        return True
        return False
        