class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.checkPrune(root)
        
    def checkPrune(self, root: Optional[TreeNode]):
        if not root:
            return None

        root.left = self.checkPrune(root.left)
        root.right = self.checkPrune(root.right)

        if not root.left and not root.right and not root.val:
            return None
        return root
        
        
            
        