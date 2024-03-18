from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 4:
            return res
        elif n == 4:
            res.append(nums)
            return res if sum(nums) == target else []
        nums.sort()
        for i in range(len(nums) - 3):

            for j in range(i + 1, len(nums) - 2):

                k = j + 1
                l = n - 1

                while k < l:

                    sum4 = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum4 < target:
                        k += 1
                    elif sum4 > target:
                        l -= 1
                    else:
                        app = [nums[i], nums[j], nums[k], nums[l]]
                        if app not in res:
                            res.append(app)

                        temp_k = k
                        temp_l = l
                        while k < l and nums[k] == nums[temp_k]:
                            k += 1
                        while k < l and nums[l] == nums[temp_l]:
                            l -= 1

                while j + 1 < n and nums[j] == nums[j - 1]:
                    j += 1

            while i + 1 < n and nums[i] == nums[i - 1]:
                i += 1

        return res
