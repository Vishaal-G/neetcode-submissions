class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedP = set()
        visitedA = set()

        def dfs(row, col, visited, prevHeight):
            if (row,col) in visited:
                return 
            if row < 0 or row >= len(heights) or col >= len(heights[0]) or col < 0:
                return
            if heights[row][col] < prevHeight:
                return 
            
            visited.add((row,col))
            
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
        
        for row in range (len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    dfs(row, col, visitedP, heights[row][col])
                if row == len(heights) -1 or col == len(heights[0]) -1:
                    dfs(row,col, visitedA, heights[row][col])
    

        return [list(res) for res in visitedP & visitedA]

        
        
        


            
            

        
        