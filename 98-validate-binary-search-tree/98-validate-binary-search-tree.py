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
        
        print(root.val)
        print(min_val)
        print(max_val)
        
        if root.val <= min_val or root.val >= max_val:
            return False
        result_right = self.isValidHelper(root.right,root.val,max_val)
        result_left = self.isValidHelper(root.left,min_val,root.val)
        return result_right and result_left