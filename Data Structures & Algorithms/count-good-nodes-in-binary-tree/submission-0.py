# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = []

        def dfs(curr,largest):
            if not curr:
                return None
            if curr.val >= largest:
                self.res.append(curr.val)
                largest = curr.val
            dfs(curr.left, largest)
            dfs(curr.right, largest)
        
        dfs(root, -200)
        print(self.res)
        return len(self.res)