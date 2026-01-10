# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
from typing import Optional, List

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_deepth = -1
        node_subtree_map = {}  # {node.val: [subtree_node_id_list]}
        deepth_node_map = {}  # {deepth: [node_id_list]}
        node_deepth_map = {}  # {node.val: deepth}
        id_node_map = {}  # {node_id: node}
        
        def dfs(node: Optional[TreeNode], deepth: int) -> List[int]:
            nonlocal max_deepth, node_subtree_map, deepth_node_map, id_node_map
            if not node:
                return []
            id_node_map[node.val] = node
            if deepth not in deepth_node_map:
                deepth_node_map[deepth] = []
            deepth_node_map[deepth].append(node.val)
            node_deepth_map[node.val] = deepth
            this_id_list = [node.val]
            if node.left:
                this_id_list += dfs(node.left, deepth+1)
            if node.right:
                this_id_list += dfs(node.right, deepth+1)
            node_subtree_map[node.val] = this_id_list
            if deepth > max_deepth:
                max_deepth = deepth
            return this_id_list
        
        dfs(root, 0)
        max_deepth_nodes = deepth_node_map[max_deepth]
        max_parent_node_deepth = -1
        max_parent_node_id = -1
        set_max_deepth_nodes = set(max_deepth_nodes)
        for node_id, node_list in node_subtree_map.items():
            set_node_list = set(node_list)
            if set_max_deepth_nodes.issubset(set_node_list):
                current_deepth = node_deepth_map[node_id]
                if current_deepth > max_parent_node_deepth:
                    max_parent_node_deepth = current_deepth
                    max_parent_node_id = node_id
        res_node = id_node_map[max_parent_node_id]
        return res_node

if __name__ == '__main__':    
    b = TreeNode(0, TreeNode(1, None, TreeNode(2)), TreeNode(3))
    res = Solution().subtreeWithAllDeepest(b)
    print(2 == res.val ,"  ", res.val)
    
    c = TreeNode(1)
    res = Solution().subtreeWithAllDeepest(c)
    print(1 == res.val ,"  ", res.val)
    
    a = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    res = Solution().subtreeWithAllDeepest(a)
    print(2 == res.val ,"  ", res.val)
    
    d = TreeNode(1, TreeNode(2, TreeNode(7), TreeNode(6)), TreeNode(3, TreeNode(4), TreeNode(5)))
    res = Solution().subtreeWithAllDeepest(d)
    print(1 == res.val,"  ", res.val)