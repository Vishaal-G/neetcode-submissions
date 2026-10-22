class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        Q = deque()
        seen = set()
        
        for row in range(len(grid)):
            for col in range (len(grid[0])):
                if grid[row][col] == 0:
                    Q.append((row, col))
                    seen.add((row, col))
        

        while Q:
            r,c = Q.popleft()

            for newRow, newCol in directions:
                nr, nc = newRow+ r, newCol + c
                if nr >= len(grid) or nr < 0 or nc >= len(grid[0]) or nc < 0:
                    continue 
                if grid[nr][nc] == -1:
                    continue 
                if (nr,nc) in seen:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                seen.add((nr, nc))
                Q.append((nr,nc))


            


        
        
             