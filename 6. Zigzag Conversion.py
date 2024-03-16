class Solution:
    def convert(self, s: str, numRows: int) -> str:

        elems_in_col = numRows
        elems_in_zig = elems_in_col - 2

        if elems_in_zig < 0:
            elems_in_zig = 0

        res = ""
        step = elems_in_col + elems_in_zig

        for nr_row in range(numRows):
            idx = nr_row
            while idx < len(s):
                res += s[idx]
                if 1 <= nr_row <= elems_in_zig:
                    zig_idx = idx + (step - 2 * nr_row)
                    if zig_idx < len(s):
                        res += s[zig_idx]

                idx += step

        return res
