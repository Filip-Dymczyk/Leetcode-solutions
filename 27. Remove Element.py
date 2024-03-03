from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        left_pointer = 0
        right_pointer = n - 1
        while left_pointer <= right_pointer:
            if nums[left_pointer] == val:
                if nums[right_pointer] != val:
                    nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                right_pointer -= 1
            else:
                k += 1
                left_pointer += 1
        return k
    