from types import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = {}
        
        def dfs(node, level):
            if not node:
                return
            if level not in level_sum:
                level_sum[level] = 0
            level_sum[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 1)
        max_sum = float("-inf")
        result = 0
        for level,sum in level_sum.items():
            if sum > max_sum:
                max_sum = sum
                result = level
        return result

