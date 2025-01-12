# Question Link: https:#leetcode.com/problems/maximum-frequency-stack/
from typing import *
from collections import defaultdict, Counter

class FreqStack(object):

    def __init__(self):
        self.freq_map = Counter()
        self.freq_stack = defaultdict(list)
        self.max_freq = -1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq_map[val] += 1
        self.max_freq = max(self.freq_map[val], self.max_freq)
        self.freq_stack[self.freq_map[val]].append(val)

        return


    def pop(self):
        """
        :rtype: int
        """
        entry = self.freq_stack[self.max_freq].pop()
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1

        self.freq_map[entry] -= 1
        return entry





if __name__ == "__main__":
    freqStack = FreqStack()
    freqStack.push(5) # The stack is [5]
    freqStack.push(7) # The stack is [5,7]
    freqStack.push(5) # The stack is [5,7,5]
    freqStack.push(7) # The stack is [5,7,5,7]
    freqStack.push(4) # The stack is [5,7,5,7,4]
    freqStack.push(5) # The stack is [5,7,5,7,4,5]
    freqStack.pop()   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop()   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop()   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop()   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the
    print('TIME COMPLEXITY: O(1)')
    print('SPACE COMPLEXITY: O(n)')