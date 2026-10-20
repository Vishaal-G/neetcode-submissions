class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def numIslandsHelper(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return
            
            if grid[row][col] == "0":
                return

            #Mark current spot to zero to prevent infinte recursion
            grid[row][col] = "0"
            numIslandsHelper(row + 1, col)
            numIslandsHelper(row - 1, col)
            numIslandsHelper(row, col + 1)
            numIslandsHelper(row, col - 1)

        count = 0
        for row in range (len(grid)):
            for col in range (len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    numIslandsHelper(row, col)
        return count
        