# Question Link: https://neetcode.io/problems/reverse-a-linked-list
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

if __name__ == "__main__":
    head = [0,1,2,3]
    curr_node = ListNode(head[0])
    head_node = curr_node
    for value in head[1:]:
        temp = ListNode(value)
        curr_node.next = temp
        curr_node = temp

    rev_list = Solution().reverseList(head_node)
    while rev_list:
        print(rev_list.val)
        rev_list = rev_list.next
        
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')