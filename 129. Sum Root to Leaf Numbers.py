#time: O(n)
#space: O(height of recursion stack)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.totalsum=0
        self.dfs(root,0)
        return self.totalsum

    def dfs(self,root,csum):
        if(root is None):
            return
        csum= csum*10 + root.val
        if(root.left is None and root.right is None):
            self.totalsum = self.totalsum + csum
        self.dfs(root.left,csum)
        self.dfs(root.right, csum)

        return
        
