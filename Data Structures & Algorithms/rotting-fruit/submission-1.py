class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ([1,0], [-1,0], [0,1], [0,-1])
        Q = deque([])
        minutes = 0
        goodOranges = 0

        for row in range (len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    goodOranges += 1
                if grid[row][col] == 2:
                    Q.append((row, col))
        
        print(goodOranges)
        while Q:
            QLen = len(Q)
            i = 0
            isRotted = False
            while i < QLen:
                r, c = Q.popleft()
                for rowOffset, colOffset in directions:
                    newRow = r + rowOffset
                    newCol = c + colOffset
                    if newRow >= len(grid) or newRow < 0 or newCol >= len(grid[0]) or newCol < 0:
                        continue
                    if grid[newRow][newCol] == 0 or grid[newRow][newCol] == 2:
                        continue
        
                    grid[newRow][newCol] = 2
                    goodOranges -= 1
                    isRotted = True
                    Q.append((newRow, newCol))
                i += 1
            if (isRotted):
                minutes += 1
        print(goodOranges)  
        return minutes if goodOranges == 0 else -1
            




        