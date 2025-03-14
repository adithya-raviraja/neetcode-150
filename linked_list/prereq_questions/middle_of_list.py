# Question Link: https://leetcode.com/problems/middle-of-the-linked-list/description/
from typing import *

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        

if __name__ == "__main__":
    entries = [1,2,3,4,5]
    curr = ListNode(entries[0])
    head = curr
    # iterating over input list
    for i in entries[1:]:
      temp = ListNode(i)
      curr.next = temp
      curr = temp

    middle = Solution().middleNode(head)
    print('middle is: ', middle.val)


    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')