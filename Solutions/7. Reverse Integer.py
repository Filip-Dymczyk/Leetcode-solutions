class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        l = list(s)
        if s[0] == '-':
            del l[0]
            l.append('-')
        l.reverse()
        res = int(''.join(l))
        if -2**31 <= res <= 2**31 - 1:
            return res
        return 0
