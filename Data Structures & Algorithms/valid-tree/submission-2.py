class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        seen = set()

        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        if dfs(0, -1) and len(seen) == n:
            return True
        
        return False

                
        