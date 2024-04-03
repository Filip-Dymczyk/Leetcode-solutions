from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bin_search(l: int, r: int, t: int) -> int:
            m = (l + r) // 2
            if l > r:
                if l > len(nums) - 1:
                    return l
                if nums[l] > t:
                    return l if l > 0 else 0
                elif nums[l] < t:
                    if nums[r] > t:
                        return l + 1
                    return r + 1
            if nums[m] == t:
                return m
            elif nums[m] > t:
                return bin_search(l, m - 1, t)
            return bin_search(m + 1, r, t)
        return bin_search(0, len(nums) - 1, target)
    