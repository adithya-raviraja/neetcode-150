# Question Link: https://neetcode.io/problems/depth-of-binary-tree
from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        level_order_deque = deque()

        if not root:
            return level
        
        level_order_deque.append(root)

        while len(level_order_deque) > 0:
            # curr = level_order_deque.popleft()
            curr_level = len(level_order_deque)

            for i in range(curr_level):
                curr = level_order_deque.popleft()
                if curr.left:
                    level_order_deque.append(curr.left)
                if curr.right:
                    level_order_deque.append(curr.right)

            level += 1

        return level

        



if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')