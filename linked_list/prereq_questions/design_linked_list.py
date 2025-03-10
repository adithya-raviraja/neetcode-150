# Question Link: https://leetcode.com/problems/design-linked-list/description/
from typing import *

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.size or index < 0:
            return -1
        
        curr_head = self.head

        for _ in range(index):
            curr_head = curr_head.next

        return curr_head.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.addAtIndex(self.size, val)

        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        
        node = ListNode(val)
        curr_head = self.head
        if index <= 0:
            node.next = curr_head
            self.head = node
        else:
            for i in range(index - 1):
                curr_head = curr_head.next
            
            node.next = curr_head.next
            curr_head.next = node

        self.size += 1
        return

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            return
        
        curr_head = self.head
        if index == 0:
            self.head = curr_head.next
        else:
            for _ in range(index - 1):
                curr_head = curr_head.next

            curr_head.next = curr_head.next.next
        
        self.size -= 1
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == "__main__":
    print('TIME COMPLEXITY: O(n) (get, delete, insert)')
    print('SPACE COMPLEXITY: O(n)')