class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or (n % 3 != 0 and n != 1):
            return False

        while n > 3:
            n //= 3
            if n % 3 != 0:
                return False

        return True
    