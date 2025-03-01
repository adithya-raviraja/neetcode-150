# Question Link: https://neetcode.io/problems/merge-two-sorted-linked-lists
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2
        return new_head.next

        

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,5]

    curr1 = ListNode(list1[0])
    head1 = curr1

    for value in list1[1:]:
        temp1 = ListNode(value)
        curr1.next = temp1
        curr1 = temp1

    curr2 = ListNode(list2[0])
    head2 = curr2

    for value in list2[1:]:
        temp2 = ListNode(value)
        curr2.next = temp2
        curr2 = temp2
    
    merged_list = Solution().mergeTwoLists(head1, head2)
    while merged_list:
        print(merged_list.val)
        merged_list = merged_list.next
        
    print('TIME COMPLEXITY: O(m+n)')
    print('SPACE COMPLEXITY: O(1)')