from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)
        n_zeros = 0
        max_product = 1

        for i, num in enumerate(nums):
            if num == 0:
                n_zeros += 1
                if n_zeros == 2:
                    return [0] * len(nums)
            else:
                max_product *= num

        for i, num in enumerate(nums):
            if num == 0:
                answer[i] = max_product
            else:
                if n_zeros > 0:
                    answer[i] = 0
                else:
                    answer[i] = max_product // nums[i]

        return answer
