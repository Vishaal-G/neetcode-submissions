# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepthHelper(root, count):
    if root == None:
        return 0
    
    valLeft = maxDepthHelper(root.left, count+1)
    valRight = maxDepthHelper(root.right, count + 1)

    return max(valLeft, valRight) + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return maxDepthHelper(root, 0)
