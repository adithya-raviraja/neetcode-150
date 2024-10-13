# Question Link: https://leetcode.com/problems/range-sum-query-2d-immutable/description/
from typing import *

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.prefix_rows = list()
        self.prefix_cols = list()
        for row in matrix:
            total_sum = 0
            row_entry = list()
            for i in range(0, len(row)):
                total_sum += row[i]
                row_entry.append(total_sum)
            self.prefix_rows.append(row_entry)

        for i in range(len(matrix)):
            total_sum = 0
            col_entry = list()
            for row in matrix:
                total_sum += row[i]
                col_entry.append(total_sum)
            self.prefix_cols.append(col_entry)

        print('INPUT ARRAY')
        for row in matrix:
            print(' '.join(str(x) for x in row))
        
        print('\n')
        print('PREFIX ROWS')
        for row in self.prefix_rows:
            print(' '.join(str(x) for x in row))

        print('\n')
        print('PREFIX COLS')
        for row in self.prefix_cols:
            print(' '.join(str(x) for x in row))
   
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0

        start_row = row1
        start_col = col1
        end_row = row2
        end_col = col2

        print('PRINTING ROW INDEX: ')
        while start_row <= end_row:
            print(start_row, start_col, end_row, end_col)
            prefix_right = self.prefix_rows[start_row][end_col]
            prefix_left = self.prefix_rows[start_row][start_col - 1] if start_col > 0 else 0
            sum += prefix_right - prefix_left
            start_row += 1

        start_row = row1
        return int(sum)

if __name__ == "__main__":
    input = [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
    class_inst = NumMatrix(input[0][0])
    for i in range(1, len(input)):
        sum = class_inst.sumRegion(input[i][0], input[i][1], input[i][2], input[i][3])
        print(f'SUM REGION: {input[i]}: {sum}')
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')