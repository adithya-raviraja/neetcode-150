# Question Link: https://neetcode.io/problems/add-two-numbers
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val = list()
        l2_val = list()
        
        while l1:
            l1_val.insert(0, str(l1.val))
            l1 = l1.next

        l1_val = int(''.join(l1_val))
        
        while l2:
            l2_val.insert(0, str(l2.val))
            l2 = l2.next

        l2_val = int(''.join(l2_val))

        two_sum = l1_val + l2_val
        head = None
        curr = None
        counter = 0
        if two_sum == 0:
            head = ListNode(two_sum)
        else:
            while two_sum > 0:
                digit = two_sum % 10
                if counter == 0:
                    curr = ListNode(digit)
                    head = curr
                    counter += 1
                else:
                    tmp = ListNode(digit)
                    curr.next = tmp
                    curr = tmp

                two_sum //= 10

        return head

if __name__ == "__main__":
    l1 = [0]
    curr = ListNode(l1[0])
    l1_head = curr
    # iterating over input list
    for i in l1[1:]:
      temp = ListNode(i)
      curr.next = temp
      curr = temp

    l2 = [0]
    curr = ListNode(l2[0])
    l2_head = curr
    # iterating over input list
    for i in l2[1:]:
      temp = ListNode(i)
      curr.next = temp
      curr = temp

    output = Solution().addTwoNumbers(l1_head, l2_head)
    while output:
        print(output.val)
        output = output.next
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')