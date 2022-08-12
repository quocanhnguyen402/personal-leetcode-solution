# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.findAnswer(root,max(q.val,p.val),min(q.val,p.val))
        
    def findAnswer(self,root,big_val,min_val):
        if root.val < min_val:
            return self.findAnswer(root.right,big_val,min_val)
        if root.val > big_val:
            return self.findAnswer(root.left,big_val,min_val)
        return root