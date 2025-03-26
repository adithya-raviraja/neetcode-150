# Question Link: https://neetcode.io/problems/merge-k-sorted-linked-lists
from typing import *
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        

        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i - 1], lists[i])

        return lists[-1]

    def mergeLists(self, l1, l2):
        head = ListNode(0)
        curr = head

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        
        if l2: 
            curr.next = l2

        return head.next


if __name__ == "__main__":
    lists = [[1,2,4],[1,3,5],[3,6]]
    linked_list = list()
    for list_entry in lists:
        head = copy.deepcopy(ListNode(0))
        curr = head
        for entry in list_entry:
            curr.next = ListNode(entry)
            curr = curr.next

        linked_list.append(head.next)
    
    merged_list = Solution().mergeKLists(linked_list)
    curr = merged_list
    while curr:
        print(curr.val)
        curr = curr.next

    print('TIME COMPLEXITY: O(n*log(k))')
    print('SPACE COMPLEXITY: O(1)')