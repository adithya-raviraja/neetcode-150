# Question Link: https://neetcode.io/problems/reorder-linked-list
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



if __name__ == "__main__":
    entries = [2,4,6,8,10]
    curr = ListNode(entries[0])
    head = curr
    # iterating over input list
    for i in entries[1:]:
      temp = ListNode(i)
      curr.next = temp
      curr = temp

    output = Solution().reorderList(head)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')