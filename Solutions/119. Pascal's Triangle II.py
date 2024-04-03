from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev_row = [1, 1]
        res_row = []

        i = 1

        while i < rowIndex + 1:
            res_row = [1]
            for col_index in range(1, i):
                res_row.append(prev_row[col_index - 1] + prev_row[col_index])
            res_row.append(1)
            prev_row = res_row
            i += 1

        return res_row if len(res_row) > 0 else prev_row
