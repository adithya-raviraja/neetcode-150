# Question Link: 
from typing import *

# Definition for a Node.
class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        node_map = dict()
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            new_list = node_map[curr]
            if curr.next is not None:
                new_list.next = node_map[curr.next]
            else:
                new_list.next = None
            if curr.random is not None:
                new_list.random = node_map[curr.random]
            else:
                new_list.random = None
            curr = curr.next

        return node_map.get(head)

if __name__ == "__main__":
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')