# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equal(self, p, q):
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False

        return self.equal(p.left, q.left) and self.equal(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.equal(p, q)