# Question Link: 
from typing import *
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        total_sub_arrays = 0
        window = 0
        list_sum = 0
        L = 0

        for R in range(len(arr)):
            if R - L + 1 > k:
                window -= 1
                list_sum -= arr[L]
                L += 1

            window += 1
            list_sum += arr[R]
            if window == k:
                avg = list_sum/k
                if avg >= threshold:
                    total_sub_arrays += 1

        return total_sub_arrays

if __name__ == "__main__":
    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
    output = Solution().numOfSubarrays(arr, k, threshold)
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')