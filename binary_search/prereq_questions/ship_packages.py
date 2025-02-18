# Question Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
from typing import *

class Solution(object):
    def daysToProcess(self, weights, ship_weight):
        days = 0
        cuml_weight = 0

        for day_weight in weights:
            if cuml_weight + day_weight > ship_weight:
                cuml_weight = day_weight
                days += 1
                continue
            elif cuml_weight + day_weight == ship_weight:
                cuml_weight = 0
                days += 1
                continue
            else:
                cuml_weight += day_weight

        if cuml_weight > 0:
            days += 1

        return days


    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        total_packages_weight = sum(weights)
        max_weight = max(weights)
        min_days = total_packages_weight

        low = max_weight
        high = total_packages_weight
        
        while low <= high:
            mid = (low + high) // 2
            total_days = self.daysToProcess(weights, mid)
            if total_days <= days:
                min_days = mid
                high = mid - 1
            else:
                low = mid + 1

        return min_days

if __name__ == "__main__":
    weights = [3,3,3,3,3,3]
    days = 2

    output = Solution().shipWithinDays(weights, days)
    print('MIN_DAYS: ', output)
    print('TIME COMPLEXITY: O(mlog(n))')
    print('SPACE COMPLEXITY: O(1)')