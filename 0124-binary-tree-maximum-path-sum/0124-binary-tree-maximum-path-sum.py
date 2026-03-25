# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float("-inf")
        self.solve(root)
        return self.maxsum
    
    def solve(self,root):
        if root is None:
            return 0
        leftsum = self.solve(root.left)
        if leftsum < 0:
            leftsum = 0
        rightsum = self.solve(root.right)
        if rightsum < 0:
            rightsum = 0
        self.maxsum = max(self.maxsum,leftsum+root.val+rightsum)
        return root.val + max(leftsum,rightsum)