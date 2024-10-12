# Question Link: https://leetcode.com/problems/range-sum-query-immutable/
from typing import *

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = list()
        total_sum = 0
        for i in range(0, len(nums)):
            total_sum += nums[i]
            self.prefix.append(total_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prefix_right = self.prefix[right]
        prefix_left = self.prefix[left - 1] if left > 0 else 0

        return prefix_right - prefix_left
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    input = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

    class_inst = NumArray(input[0][0])
    for i in range(1, len(input)):
        sub_array = input[i]
        sub_array_total = class_inst.sumRange(sub_array[0], sub_array[1])
        print('SUB_ARRAY: ', sub_array, ' sum: ', sub_array_total)
        i = i + 1

    print('TIME COMPLEXITY: O(1)')
    print('SPACE COMPLEXITY: O(n)')