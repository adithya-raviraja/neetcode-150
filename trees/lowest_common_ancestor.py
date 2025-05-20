# Question Link: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
from typing import *
from trees.common import *

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

if __name__ == "__main__":
    root = [5,3,8,1,4,7,9,None,2]
    p = 3
    q = 8

    root = construct_binary_tree(root)
    output = Solution().lowestCommonAncestor(root, p, q)
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')