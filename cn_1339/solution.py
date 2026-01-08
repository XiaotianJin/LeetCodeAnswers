# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_product = float('-inf')
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        all_children_sum = []
        
        def dfs_sum(node):
            if node is None:
                return 0

            left_sum = dfs_sum(node.left)
            right_sum = dfs_sum(node.right)
            all_children_sum.append(left_sum)
            all_children_sum.append(right_sum)

            return left_sum + right_sum + node.val
        
        total_sum = dfs_sum(root)
        for child_sum in all_children_sum:
            self.max_product = max(self.max_product, child_sum * (total_sum - child_sum))
        
        return self.max_product % (10**9+7)


if __name__ == '__main__':    
    b = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
    print(Solution().maxProduct(b))  # Output: 90
    
    a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
    print(Solution().maxProduct(a)) # Output: 110