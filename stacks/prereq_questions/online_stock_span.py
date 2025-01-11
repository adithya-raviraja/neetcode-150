# Question Link: https://leetcode.com/problems/online-stock-span/description/
from typing import *
import copy

class StockSpanner(object):

    def __init__(self):
        self.span_stack = list()

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1

        while self.span_stack and self.span_stack[-1][0] <= price:
            span += self.span_stack.pop()[1]

        span_entry = [price, span]
        self.span_stack.append(span_entry)
        
        return span
        
if __name__ == "__main__":
    entries = [[100], [80], [60], [70], [60], [75], [85]]
    stock_spanner = StockSpanner()
    final_output = []

    for entry in entries:
        final_output.append(stock_spanner.next(entry[0]))
    
    print(final_output)

    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')