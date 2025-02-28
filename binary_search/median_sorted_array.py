# Question Link: 
from typing import *
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a_arr, b_arr = nums1, nums2
        if len(a_arr) > len(b_arr):
            a_arr, b_arr = b_arr, a_arr

        low = 0
        high = len(a_arr) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            mid_left = (low + high) // 2
            mid_right = half - mid_left - 2

            a_left = a_arr[mid_left] if mid_left >= 0 else float('-infinity')
            a_right = a_arr[mid_left + 1] if (mid_left + 1) < len(a_arr) else float('infinity')

            b_left = b_arr[mid_right] if mid_right >=0 else float('-infinity')
            b_right = b_arr[mid_right + 1] if (mid_right + 1) < len(b_arr) else float('infinity')

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left < b_right:
                low = mid_left + 1
            else:
                high = mid_left - 1



if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2,4]
    output = Solution().findMedianSortedArrays(nums1, nums2)
    print('OUTPUT: ', output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')