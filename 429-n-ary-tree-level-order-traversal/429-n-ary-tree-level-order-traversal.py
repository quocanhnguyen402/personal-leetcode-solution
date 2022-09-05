"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        def addNode(root,level):
            if root == None:
                return result
            layer = []
            if len(result) == level:
                result.append([root.val])
            else:
                result[level].append(root.val)
            if root.children:
                for node in root.children:
                    addNode(node,level+1)
        addNode(root,0)
        return result
                    
    
        