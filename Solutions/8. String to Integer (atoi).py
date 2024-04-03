class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if len(s) == 0:
            return 0

        sign = -1 if s[0] == "-" else 1

        if s[0] in ["-", "+"]:
            s = s[1:]

        num = ""
        i = 0

        while i < len(s) and s[i].isnumeric():
            num += s[i]
            i += 1

        if not num:
            return 0

        num = sign * int(num)

        if num < -2 ** 31:
            num = -2 ** 31
        if num > 2 ** 31 - 1:
            num = 2 ** 31 - 1

        return num
