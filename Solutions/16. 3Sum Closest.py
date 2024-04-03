from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0
        elif n == 3:
            return sum(nums)

        nums.sort()

        res = float('inf')

        for current, curr_value in enumerate(nums):
            if current > 0 and nums[current] == nums[current - 1]: continue

            left = current + 1
            right = n - 1

            while left < right:

                sum3 = curr_value + nums[left] + nums[right]

                if abs(target - sum3) < abs(target - res):
                    res = sum3

                if sum3 > target:
                    right -= 1
                elif sum3 < target:
                    left += 1
                else:
                    return sum3

        return res
