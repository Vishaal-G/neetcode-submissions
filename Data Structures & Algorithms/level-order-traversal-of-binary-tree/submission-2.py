# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return []
        Q = deque([root])

        
        while Q:
            levelNodes = []
            sizeOfLevel = len(Q)

            for i in range (sizeOfLevel):
                val = Q.popleft()

                if val.left:
                    Q.append(val.left)
                
                if val.right:
                    Q.append(val.right)
                
                levelNodes.append(val.val)
            res.append(levelNodes)
        return res

            
            

            



        
        
