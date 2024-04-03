class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        was_changed = False
        while n > 1:
            if n % 2 == 0:
                n //= 2
                was_changed = True
            if n % 3 == 0:
                n //= 3
                was_changed = True
            if n % 5 == 0:
                n //= 5
                was_changed = True
            if not was_changed:
                return False
            was_changed = False
        return True
