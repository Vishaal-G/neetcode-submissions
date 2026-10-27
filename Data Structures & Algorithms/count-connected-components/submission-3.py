class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for f, t in edges:
            adjList[f].append(t)
            adjList[t].append(f)        
        
        self.numPaths = 0
        seen = set()
        def countComponentsHelper(node):
            if node in seen:
                return

            seen.add(node)
            for nei in adjList[node]:
                countComponentsHelper(nei)
        
        for i in range (n):
            if i not in seen:
                self.numPaths += 1
            countComponentsHelper(i)


        return self.numPaths
        