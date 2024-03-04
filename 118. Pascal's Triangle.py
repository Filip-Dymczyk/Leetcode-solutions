from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Result List:
        res = []

        # Row iterator:
        i = 0

        while i < numRows:
            if i == 0:
                res.append([1])
            else:
                # First one in helper_tab:
                helper_tab = [1]

                # Adding elements (apart from ones) into row:
                for num_col in range(1, i):
                    helper_tab.append(res[i - 1][num_col - 1] + res[i - 1][num_col])

                # Last one in helper_tab:
                helper_tab.append(1)

                # Adding helper_tab into result
                res.append(helper_tab)
            i += 1
        return res
