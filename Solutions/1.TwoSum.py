from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating dictionary mapping target-elem value on its index in the array:
        map_to_target = dict()

        for idx, number in enumerate(nums):
            complementary_value = target - number

            # We found a number that is complementary to one seen before:
            if number in map_to_target:
                return [map_to_target[number], idx]

            # We add complementary value to current number:
            if complementary_value not in map_to_target:
                map_to_target[complementary_value] = idx
