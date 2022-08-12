# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        bigger_val = max(q.val,p.val)
        lower_val = min(q.val,p.val)

        if root.val < lower_val:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val > bigger_val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root