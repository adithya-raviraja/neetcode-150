# Question Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
from typing import *

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head
        sum_dict = dict()
        total_count = 0
        max_sum = 0

        while curr:
            sum_dict[total_count] = curr.val
            curr = curr.next
            total_count += 1

        for i in range(int(total_count/2)):
            twin_val = (total_count - 1 - i)
            curr_sum = sum_dict[i] + sum_dict[twin_val]
            if max_sum < curr_sum:
                max_sum = curr_sum
        
        # print(sum_list)
        return max_sum


if __name__ == "__main__":
    entries = [4,2,2,3]
    curr = ListNode(entries[0])
    head = curr
    # iterating over input list
    for i in entries[1:]:
      temp = ListNode(i)
      curr.next = temp
      curr = temp
    
    max_pair_sum = Solution().pairSum(head)
    print('MAX_PAIR_SUM: ', max_pair_sum)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')