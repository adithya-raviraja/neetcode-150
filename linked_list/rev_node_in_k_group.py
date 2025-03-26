# Question Link: https://neetcode.io/problems/reverse-nodes-in-k-group
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_subset(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def get_subset(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

if __name__ == "__main__":
    head = [1,2,3,4,5,6], k = 3
    list_head = ListNode()
    curr = list_head

    for entry in head:
        curr.next = ListNode(entry)
        curr = curr.next

    rev_list = Solution().reverseKGroup(list_head, k)
    curr = rev_list

    while curr:
        print(curr.val)
        curr = curr.next

    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')