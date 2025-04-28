# Question Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        postorder = list()
        stack = list()
        entry = {
            'node': root,
            'visited': False
        }
        
        stack.append(entry)
        
        while stack:
            stack_entry = stack.pop()
            curr, visited = stack_entry['node'], stack_entry['visited']
            if visited:
                postorder.append(curr.val)
            else:
                if curr:
                    entry = {
                        'node': curr,
                        'visited': True
                    }
                    stack.append(entry)
                else:
                    continue
                if curr.right:
                    entry = {
                        'node': curr.right,
                        'visited': False
                    }
                    stack.append(entry)
                if curr.left:
                    entry = {
                        'node': curr.left,
                        'visited': False
                    }
                    stack.append(entry)
        
        return postorder

if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')