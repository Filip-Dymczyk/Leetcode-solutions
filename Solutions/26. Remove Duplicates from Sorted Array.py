from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_elem = nums[0]
        last_idx = 0
        for num in nums[1:]:
            if num != last_elem:
                last_elem = num
                last_idx += 1
                nums[last_idx] = last_elem
        return last_idx + 1