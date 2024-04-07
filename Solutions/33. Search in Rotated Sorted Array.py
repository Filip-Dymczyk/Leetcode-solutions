from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(l: int, r: int) -> int:
            m = (l + r) // 2
            if l > r:
                return - 1
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return bin_search(l, m - 1)
            return bin_search(m + 1, r)

        if nums[0] < nums[-1]:
            return bin_search(0, len(nums) - 1)

        def bin_search_pivot(l: int, r: int) -> int:
            m = (l + r) // 2
            if (m == len(nums) - 1 or nums[m] > nums[m + 1]) and (m == 0 or nums[m] > nums[m - 1]):
                return m
            if (m == len(nums) - 1 or nums[m] < nums[m + 1]) and nums[m] < nums[0]:
                return bin_search_pivot(l, m - 1)
            return bin_search_pivot(m + 1, l)

        p = bin_search_pivot(0, len(nums) - 1)
        if target > nums[0]:
            return bin_search(0, p)
        elif target < nums[0]:
            return bin_search(p + 1, len(nums) - 1)
        return 0
