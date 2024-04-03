from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_idx = 0

        while target < matrix[row_idx][0] or target > matrix[row_idx][-1]:
            row_idx += 1
            if row_idx == len(matrix):
                return False

        row = matrix[row_idx]
        l_p = 0
        r_p = len(row) - 1

        while l_p <= r_p:
            m = (l_p + r_p) // 2

            if row[m] == target:
                return True
            elif row[m] > target:
                r_p = m - 1
            else:
                l_p = m + 1

        return False
