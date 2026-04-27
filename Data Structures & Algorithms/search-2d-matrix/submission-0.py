class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLow1, colLow2 = 0,0
        rowHigh1 = len(matrix) - 1
        colHigh2 =  len(matrix[0])-1
        middle1 = 0
        while rowLow1 <= rowHigh1:
            middle1 = (rowLow1 + rowHigh1) // 2 

            if matrix[middle1][0] <= target and target <= matrix[middle1][-1]:
                break
            elif matrix[middle1][0] > target:
                rowHigh1 = middle1 - 1
            else:
                rowLow1 = middle1 + 1
            
        while colLow2 <= colHigh2:
            middle2 = (colLow2 + colHigh2) // 2

            if matrix[middle1][middle2] > target:
                colHigh2 = middle2 - 1
            elif matrix[middle1][middle2] < target:
                colLow2 = middle2 + 1
            else:
                return True
        return False