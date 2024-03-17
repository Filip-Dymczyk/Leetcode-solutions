from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l_p = 0
        r_p = len(height) - 1
        max_area = 0

        while l_p < r_p:
            max_area = max(max_area, min(height[l_p], height[r_p]) * (r_p - l_p))

            if height[l_p] > height[r_p]:
                r_p -= 1
            else:
                l_p += 1
        return max_area
