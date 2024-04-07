from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        left_end = 0
        res = []
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                if m == 0 or nums[m - 1] != target:
                    res.append(m)
                    left_end = m
                    if m == len(nums) - 1 or nums[m + 1] != target:
                        return res + res
                    break
                else:
                    r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        l = left_end
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                if m == len(nums) - 1 or nums[m + 1] != target:
                    res.append(m)
                    if m == 0 or nums[m - 1] != target:
                        return res + res
                    break
                else:
                    l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return res if res else [-1, -1]
