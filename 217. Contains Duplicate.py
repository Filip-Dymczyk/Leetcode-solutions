from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i = 0
        j = len(nums) - 1
        seen = set()

        while i <= j:
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True

            if nums[j] not in seen:
                seen.add(nums[j])

                # Protection against having the same element checked by i and j:
            elif j != i:
                return True
            i += 1
            j -= 1

        return False
