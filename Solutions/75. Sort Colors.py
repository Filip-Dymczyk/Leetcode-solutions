from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        zeros_set = False
        while i < j:
            if nums[i] == 2:
                while j > i and nums[j] == 2:
                    j -= 1
                if j <= i:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                continue
            elif not zeros_set and nums[i] == 1:
                k = i
                while k < len(nums) and nums[k] != 0:
                    k += 1
                if k == len(nums):
                    zeros_set = True
                else:
                    nums[i], nums[k] = nums[k], nums[i]
            i += 1

            low, mid, high = 0, 0, len(nums) - 1

        # Dutch National Flag algorithm
        # while mid <= high:
        #     if nums[mid] == 0:
        #         nums[low], nums[mid] = nums[mid], nums[low]
        #         low += 1
        #         mid += 1
        #     elif nums[mid] == 1:
        #         mid += 1
        #     else:
        #         nums[mid], nums[high] = nums[high], nums[mid]
        #         high -= 1
