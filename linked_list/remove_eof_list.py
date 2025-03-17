# Question Link: https://neetcode.io/problems/remove-node-from-end-of-linked-list
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        dummy = ListNode(0, head)
        second = dummy

        while n > 0:
            first = first.next
            n -= 1

        while first:
            first = first.next
            second = second.next
    
        second.next = second.next.next
        return dummy.next

if __name__ == "__main__":
    entries = [1,2,3,4]
    n = 2
    curr = ListNode(entries[0])
    head = curr
    # iterating over input list
    for i in entries[1:]:
      temp = ListNode(i)
      curr.next = temp
      curr = temp

    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')