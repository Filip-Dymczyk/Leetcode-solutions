from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l_end = 0
        r_end = 0
        while r_end < len(nums):
            if r_end < len(nums) - 1 and nums[r_end + 1] == nums[r_end] + 1:
                r_end += 1
            else:
                if r_end == l_end:
                    res.append(f"{nums[l_end]}")
                else:
                    res.append(f"{nums[l_end]}->{nums[r_end]}")
                r_end += 1
                l_end = r_end
        return res
