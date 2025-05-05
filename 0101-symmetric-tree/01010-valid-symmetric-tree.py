# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, a, b):
        if a is None and b is None:
            return True
        
        if a is None or b is None:
            return False

        if a.val != b.val:
            return False

        return(
            self.isMirror(a.left, b.right) and
            self.isMirror(a.right, b.left)
            )
    