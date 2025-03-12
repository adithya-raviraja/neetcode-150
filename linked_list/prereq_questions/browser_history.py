# Question Link: https://leetcode.com/problems/design-browser-history/
from typing import *

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        node = ListNode(homepage)
        self.curr = node
        self.tail = node
        self.last_site = node
        self.size = 1
        curr_history = list()
        curr_history.append(node.val)
        print(f'Initial Brower History: {curr_history}')
    
    def __get_browser_history(self):
        site_list = list()
        curr_head = self.head
        while curr_head:
            site_list.append(curr_head.val)
            curr_head = curr_head.next
        return site_list

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        node = ListNode(url)
        curr_head = self.head
        # if self.last_site.val == node.val:
        #     print(f'Visited site the last site itself Url: {url}, browser_history: {self.__get_browser_history()}')
        #     return
        
        while curr_head and curr_head.val != self.last_site.val:
            curr_head = curr_head.next
        
        node.prev = curr_head
        curr_head.next = node
        self.last_site = node
        self.size += 1

        print(f'Visited: {url}, browser_history: {self.__get_browser_history()}')
        return
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        curr_site = self.last_site
        actual_steps = 0
        while actual_steps < steps:
            if not curr_site.prev:
                break
            curr_site = curr_site.prev
            actual_steps += 1

        self.last_site = curr_site
        print(f'Went back to {steps} steps to {curr_site.val}')
        return curr_site.val


    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        curr_site = self.last_site
        actual_steps = 0
        while actual_steps < steps:
            if not curr_site.next:
                break
            curr_site = curr_site.next
            actual_steps += 1
        
        self.last_site = curr_site
        print(f'Went forward to {steps} steps to {curr_site.val}')
        return curr_site.val

if __name__ == "__main__":
    # ops = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    # entries = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
    ops = ["BrowserHistory","visit","visit","visit","back","visit","forward","visit","forward","back","back"]
    entries = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],["facebook.com"],[1],["linkedin.com"],[2],[2],[7]]

    browser_inst = None
    output_list = list()
    for index, value in enumerate(ops):
        if value == "BrowserHistory":
            browser_inst = BrowserHistory(entries[index][0])
            output_list.append(None)
        elif value == "visit":
            browser_inst.visit(entries[index][0])
            output_list.append(None)
        elif value == "back":
            site = browser_inst.back(entries[index][0])
            output_list.append(site)
        elif value == "forward":
            site = browser_inst.forward(entries[index][0])
            output_list.append(site)
    
    print(output_list)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')