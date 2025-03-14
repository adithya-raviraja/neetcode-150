# Question Link: https://leetcode.com/problems/linked-list-cycle-ii/ 
from typing import *
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        
        if not fast or not fast.next:
            return None
        
        slow2 = head

        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow

if __name__ == "__main__":
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')