import numpy as np
from typing import List
import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            # Swap corners:
            matrix[i][i], matrix[i][(n - i) - 1], matrix[(n - i) - 1][i], matrix[(n - i) - 1][(n - i) - 1] = \
            matrix[(n - i) - 1][i], matrix[i][i], matrix[(n - i) - 1][(n - i) - 1], matrix[i][(n - i) - 1]

            for j in range((n - i) - 2):
                matrix[i][j + 1], matrix[j + 1][(n - i) - 1], matrix[(n - i) - 1][(n - i) - 1 - (j + 1)], matrix[(n - i) - 1 - (j + 1)][i] = matrix[(n - i) - 1 - (j + 1)][i],  matrix[i][j + 1],  matrix[j + 1][(n - i) - 1], matrix[(n - i) - 1][(n - i) - 1- (j + 1)]


matrix =[[1,2,3],[4,5,6],[7,8,9]]
S = Solution()
S.rotate(matrix)
#print(matrix)
print(np.array([[5,1,9,11, 1],[2,4,8,10, 3],[13,3,6,7, 4],[15,14,12,16, 7], [2, 8, 9, 1, 0]]))
print(np.array([[2,15,13,2,5],[8,16,3,14,1],[9,12,6,8,9],[1,7,4,10,11],[0,7,4,3,1]]))
print(np.array([[2,15,13,2,5],[8,14,3,4,1],[9,12,6,8,9],[1,16,7,10,11],[0,7,4,3,1]]))