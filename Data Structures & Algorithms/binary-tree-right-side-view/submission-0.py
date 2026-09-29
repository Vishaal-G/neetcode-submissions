# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        Q = deque([root])

        while Q:
            subLevelNodes = []
            QLen = len(Q)

            for i in range (QLen):
                val = Q.popleft()
                subLevelNodes.append(val.val)

                if val.left:
                    Q.append(val.left)
                
                if val.right:
                    Q.append(val.right)
            
            res.append(subLevelNodes[-1])
        
        return res


            
