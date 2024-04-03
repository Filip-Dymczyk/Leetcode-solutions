class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        # Scaling ascii codes so that A -> 1:
        ascii_A = ord('A') - 1

        # Base number:
        base = 26

        # Idx for iteration and n for keeping "weight" of a letter
        idx = 0
        n = len(columnTitle) - 1
        while idx < len(columnTitle):
            res += (ord(columnTitle[idx]) - ascii_A) * base ** n
            idx += 1
            n -= 1
        return res
