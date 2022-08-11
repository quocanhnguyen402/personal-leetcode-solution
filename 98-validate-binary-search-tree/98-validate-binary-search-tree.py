# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidHelper(root,-inf,inf)
        
    def isValidHelper(self, root: Optional[TreeNode],min_val,max_val)-> bool:
        if root is None:
            return True
        
        if root.val <= min_val or root.val >= max_val:
            return False

        return self.isValidHelper(root.right,root.val,max_val) and self.isValidHelper(root.left,min_val,root.val)