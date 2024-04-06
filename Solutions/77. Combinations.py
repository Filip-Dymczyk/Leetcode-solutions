from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n + 1)
        res = []

        def rec_combine(idx: int, temp: List[int]) -> None:
            if len(temp) == k:
                res.append(temp[:])
                return
            for i in range(idx, n):
                temp.append(nums[i])
                idx += 1
                rec_combine(idx, temp)
                temp.pop()
                idx = i + 1

        rec_combine(0, [])
        return res
