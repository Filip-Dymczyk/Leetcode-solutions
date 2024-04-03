class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first = 1
        last = x
        while first <= last:
            m = int((first + last) / 2)
            if m * m == x:
                return m
            elif m * m > x:
                last = m - 1
            else:
                first = m + 1
        return first - 1
    