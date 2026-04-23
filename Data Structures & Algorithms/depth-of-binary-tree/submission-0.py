# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthHelper(self, curr: Optional[TreeNode], currDepth: int):
        if curr == None:
            return currDepth
        
        return max(self.maxDepthHelper(curr.left, currDepth + 1), self.maxDepthHelper(curr.right, currDepth + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root, 0)
        