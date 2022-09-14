# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = [0]*9
        def dfs(root: Optional[TreeNode], count):
            count[root.val - 1] += 1
            if root.left == None and root.right == None:
                if checkPanlindrome(count):
                    self.result += 1
            if root.left:
                dfs(root.left,count)
            if root.right:
                dfs(root.right,count)
            count[root.val - 1] -= 1
        def checkPanlindrome(count):
            odd_count = 0
            for i in range(len(count)):
                if count[i] % 2 != 0:
                    if odd_count == 0:
                        odd_count = 1
                    else:
                        return False
            return True
        dfs(root,count)
        return self.result
        