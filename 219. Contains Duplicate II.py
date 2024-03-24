from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for idx, num in enumerate(nums):
            if num not in d:
                d[num] = idx
            else:
                if abs(d[num] - idx) <= k:
                    return True
                else:
                    d[num] = idx
        return False
