# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.solve(root,self.diameter)
        return self.diameter

    
    def solve(self,root,diameter):
        if root is None:
            return 0
        lh = self.solve(root.left,diameter)
        rh = self.solve(root.right,diameter)
        self.diameter = max(self.diameter,(lh+rh))
        return 1 + max(lh,rh)
        