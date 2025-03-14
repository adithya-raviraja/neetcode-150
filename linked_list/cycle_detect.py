# Question Link: https://neetcode.io/problems/linked-list-cycle-detection
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False


if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')