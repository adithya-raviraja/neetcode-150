# Question Link: https://neetcode.io/problems/same-binary-tree
from typing import *
from trees.common import *


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p != None and q == None) or (q != None and p == None):
            return False
        if (p == None and q == None):
            return True
        if (p.val != q.val):
            return False

        left_res = self.isSameTree(p.left, q.left)
        right_res = self.isSameTree(p.right, q.right)
        if left_res is False:
            return False
        elif right_res is False:
            return False
        else:
            return True

if __name__ == "__main__":
    p = [1,2,3]
    q = [1,2,3]

    output = Solution().isSameTree(construct_binary_tree(p), construct_binary_tree(q))
    print(output)
    print('TIME COMPLEXITY: O(max(p,q))')
    print('SPACE COMPLEXITY: O(1)')