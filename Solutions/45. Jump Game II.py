from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        j = 1
        res = 0
        while i < len(nums) - 1:
            if i + nums[i] >= len(nums) - 1:
                res += 1
                break

            next_move = j
            curr_move = nums[j]

            while j < len(nums) and j <= nums[i] + i:
                if nums[j] + j >= curr_move:
                    next_move = j
                    curr_move = nums[j] + j
                j += 1
            i = next_move
            j = i + 1
            res += 1
        return res
