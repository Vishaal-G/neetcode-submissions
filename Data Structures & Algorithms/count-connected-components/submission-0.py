class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for f, t in edges:
            adjList[f].append(t)
            adjList[t].append(f)        
        
        self.numPaths = 0
        seen = set()
        def countComponentsHelper(node, prev):
            if node in seen:
                return
            if adjList[node] == []:
                return

            seen.add(node)
            for nei in adjList[node]:
                if nei == prev:
                    continue
                countComponentsHelper(nei, node)
        
        for i in range (n):
            if i not in seen:
                self.numPaths += 1
            countComponentsHelper(i, -1)


        return self.numPaths
        