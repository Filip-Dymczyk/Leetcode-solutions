class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x

        base = x
        res = 1
        n = abs(n)
        while n:
            if n % 2 == 0:
                base *= base
                n //= 2
            else:
                res *= base
                n -= 1
        return res
