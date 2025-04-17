# Question Link: https://neetcode.io/problems/binary-tree-right-side-view
from typing import *
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        qlen = 0
        res = list()

        while q:
            qlen = len(q)
            right_val = None
            for i in range(qlen):
                curr = q.popleft()
                if curr:
                    right_val = curr
                    q.append(curr.left)
                    q.append(curr.right)
            
            if right_val is not None:
                res.append(right_val.val)
        return res

if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')