# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:   
    def comparetree(self, tree: TreeNode, subtree: TreeNode):
        if not tree and not subtree:
            return True
        if tree and subtree and tree.val == subtree.val:
            print(tree.val,subtree.val)
            return (self.comparetree(tree.left, subtree.left)) and (self.comparetree(tree.right, subtree.right))
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.comparetree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))