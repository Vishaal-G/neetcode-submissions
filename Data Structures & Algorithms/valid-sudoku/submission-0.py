class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colDuplicate = [{} for i in range (9)]
        subSquares = [{}for i in range (9)]


        for row in range (9):
            rowDuplicate = {}
            for col in range (9):
                value = board[row][col]
                if value == ".":
                    continue
                rowDuplicate[value] = 1 + rowDuplicate.get(value, 0)
                colDuplicate[col][value] = 1 + colDuplicate[col].get(value,0)
                subSquareIndex = (row//3) * 3 + (col//3)
                subSquares[subSquareIndex][value] = 1 + subSquares[subSquareIndex].get(value,0)
                if colDuplicate[col][value] > 1:
                    return False
                if rowDuplicate[value] > 1:
                    return False
                if subSquares[subSquareIndex][value] > 1:
                    return False
        
        return True





        