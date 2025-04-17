# Question Link: https://neetcode.io/problems/level-order-traversal-of-binary-tree
from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        total_level_list = list()

        if not root:
            return total_level_list
        
        level_order_queue = deque()
        level_order_queue.append(root)

        while len(level_order_queue) > 0:
            level_list = list()
            curr_level = len(level_order_queue)

            for i in range(curr_level):
                curr = level_order_queue.popleft()
                level_list.append(curr.val)

                if curr.left:
                    level_order_queue.append(curr.left)
                if curr.right:
                    level_order_queue.append(curr.right)
            
            total_level_list.append(level_list)

        return total_level_list

if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')