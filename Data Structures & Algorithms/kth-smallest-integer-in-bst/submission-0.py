# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallestHelper(self, root, k):
        if root == None:
            return
        
        self.kthSmallestHelper(root.left, k)
        self.counter += 1

        if self.counter == k:
            self.result = root.val
        
        
        self.kthSmallestHelper(root.right, k)

        return self.result

        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.result = None
        return self.kthSmallestHelper(root, k)



