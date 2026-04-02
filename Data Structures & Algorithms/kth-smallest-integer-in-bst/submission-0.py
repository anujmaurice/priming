# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = []

        def dfs(tree):
            if not tree:
                return None
            
            dfs(tree.left)
            self.smallest.append(tree.val)
            dfs(tree.right)
        
        dfs(root)
        return self.smallest[k-1]
