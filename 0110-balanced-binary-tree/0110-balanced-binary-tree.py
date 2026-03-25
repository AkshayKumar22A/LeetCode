# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        x = self.solve(root)
        if x == -1:
            return False
        else:
            return True

    def solve(self,root):
        if root is None:
            return 0
        lh = self.solve(root.left)
        if lh == -1:
            return -1
        rh = self.solve(root.right)
        if rh == -1:
            return -1
        if abs(lh -rh) > 1:
            return -1
        return 1 + max(lh,rh)
        