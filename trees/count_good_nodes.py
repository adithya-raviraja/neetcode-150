# Question Link: https://neetcode.io/problems/count-good-nodes-in-binary-tree
from typing import *
from trees.common import *

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            res = 1 if node.val >= max_val else 0
            max_val = max(node.val, max_val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res
        
        good_nodes = dfs(root, root.val)
        return good_nodes



if __name__ == "__main__":
    root = [2,1,1,3,None,1,5]
    root = construct_binary_tree(root)
    output = Solution().goodNodes(root)
    print('OUTPUT: ', output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')