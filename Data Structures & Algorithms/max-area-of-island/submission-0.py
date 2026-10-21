class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def maxAreaOfIslandHelper(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            
            size = 1

            size += maxAreaOfIslandHelper(row + 1, col)
            size += maxAreaOfIslandHelper(row - 1, col)
            size += maxAreaOfIslandHelper(row, col + 1)
            size += maxAreaOfIslandHelper(row, col - 1)

            return size


        biggest = 0

        for row in range (len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    biggest = max(biggest, maxAreaOfIslandHelper(row, col))
        
        return biggest

        