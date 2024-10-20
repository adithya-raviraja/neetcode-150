# Question Link: https://neetcode.io/problems/valid-sudoku
from typing import *
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Iteration
        for row in board:
            row_dup_check = defaultdict(int)
            for entry in row:
                if entry in row_dup_check and entry != '.':
                    return False
                else:
                    if entry != '.':
                        row_dup_check[entry] += 1

        # Column Iteration
        for col_index in range(0, 9):
            col_dup_check = defaultdict(int)
            for row_index in range(0, 9):
                if board[row_index][col_index] in col_dup_check and board[row_index][col_index] != '.':
                    return False
                else:
                    if board[row_index][col_index] != '.':
                        col_dup_check[board[row_index][col_index]] += 1
        
        # Grid Iteration
        for grid_counter in range(0, 9, 3):
            grid_dup_check = defaultdict(int)
            entries_to_check = list()
            for iterator in range(0, 3):
                entries_to_check.append(board[grid_counter][iterator])
                entries_to_check.append(board[grid_counter + 1][iterator])
                entries_to_check.append(board[grid_counter + 2][iterator])

            # print(entries_to_check)
            for entry in entries_to_check:
                if entry in grid_dup_check and entry != '.':
                    return False
                else:
                    if entry != '.':
                        grid_dup_check[entry] += 1            


            grid_dup_check2 = defaultdict(int)
            entries_to_check2 = list()
            for iterator in range(3, 6):
                entries_to_check2.append(board[grid_counter][iterator])
                entries_to_check2.append(board[grid_counter + 1][iterator])
                entries_to_check2.append(board[grid_counter + 2][iterator])

            # print(entries_to_check2)
            for entry in entries_to_check2:
                if entry in grid_dup_check2 and entry != '.':
                    return False
                else:
                    if entry != '.':
                        grid_dup_check2[entry] += 1

            grid_dup_check3 = defaultdict(int)
            entries_to_check3 = list()
            for iterator in range(6, 9):
                entries_to_check3.append(board[grid_counter][iterator])
                entries_to_check3.append(board[grid_counter + 1][iterator])
                entries_to_check3.append(board[grid_counter + 2][iterator])

            # print(entries_to_check3)
            for entry in entries_to_check3:
                if entry in grid_dup_check3 and entry != '.':
                    return False
                else:
                    if entry != '.':
                        grid_dup_check3[entry] += 1

        return True


if __name__ == "__main__":
    # board = [["1","2",".",".","3",".",".",".","."],
    #         ["4",".",".","5",".",".",".",".","."],
    #         [".","9","8",".",".",".",".",".","3"],
    #         ["5",".",".",".","6",".",".",".","4"],
    #         [".",".",".","8",".","3",".",".","5"],
    #         ["7",".",".",".","2",".",".",".","6"],
    #         [".",".",".",".",".",".","2",".","."],
    #         [".",".",".","4","1","9",".",".","8"],
    #         [".",".",".",".","8",".",".","7","9"]]
    
    board = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","1",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
    
    for line in board:
        print(" ".join(line))
    
    output = Solution().isValidSudoku(board)
    print('IS_VALID_SUDOKU: ', output)
    print('TIME COMPLEXITY: O(n^2)')
    print('SPACE COMPLEXITY: O(1)')