import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        c = math.log(n, 4)
        return int(c) == c
