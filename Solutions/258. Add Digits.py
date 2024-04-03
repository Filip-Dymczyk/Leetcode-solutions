class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) > 1:
            num = 0
            for digit in s:
                num += int(digit)
            s = str(num)
        return num
