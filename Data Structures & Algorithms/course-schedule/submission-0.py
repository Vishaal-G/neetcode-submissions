class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        
        for node, neighbour in prerequisites:
            adjList[node].append(neighbour)
        
        visited = set() 
        def canFinishHelper(node):
            if node in visited:
                return False

            if adjList[node] == []:
                return True
            
            visited.add(node)
            
            for nei in adjList[node]:
                if not canFinishHelper(nei):
                    return False
            
            visited.remove(node)
            adjList[node] = []
            
            return True
        
        for course in range(numCourses):
            if not canFinishHelper(course):
                return False
        return True

        
        


        
