# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        result = []
        def path(root,cur_target,cur_path):
            if root is None:
                return None
            cur_path.append(root.val)
            cur_target += root.val
            if cur_target == targetSum and root.left == None and root.right == None:
                result.append(cur_path.copy())
            else:
                path(root.left,cur_target,cur_path)
                path(root.right,cur_target,cur_path)
            cur_path.pop()
        path(root,0,[])
        return result
            