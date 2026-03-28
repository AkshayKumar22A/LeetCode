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
        self.result = []
        self.solve(root,0)
        return self.result

    def solve(self,node,level):
        if node is None:
            return 
        if len(self.result) == level:
            self.result.append(node.val)
        if node.right:
            self.solve(node.right,level+1)
        if node.left:
            self.solve(node.left,level+1)
        return