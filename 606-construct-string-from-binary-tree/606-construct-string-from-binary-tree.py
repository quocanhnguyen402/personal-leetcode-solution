# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        str_result = str(root.val)
        if not root.left and not root.right:
            return str_result
        if root.left:
            str_result += "(" + self.tree2str(root.left) + ")"
        if root.right:
            if not root.left:
                str_result += "()"
            str_result += "(" + self.tree2str(root.right) + ")"
        return str_result
        