# Question Link: https://neetcode.io/problems/subtree-of-a-binary-tree
from typing import *
from trees.common import *

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot)
        

if __name__ == "__main__":
    root = [1,2,3,4,5,None,None,6]
    subRoot = [2,4,5]

    output = Solution().isSubtree(construct_binary_tree(root), construct_binary_tree(subRoot))
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')