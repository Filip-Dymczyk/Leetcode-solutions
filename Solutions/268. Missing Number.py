from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        control_sum = sum(range(len(nums) + 1))
        nums_sum = 0
        for num in nums:
            nums_sum += num
        return control_sum - nums_sum
