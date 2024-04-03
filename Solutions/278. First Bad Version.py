# The isBadVersion API is already defined for you.
#def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        r = n
        l = 1
        if l == r or isBadVersion(l):
            return l
        while l < r - 1:
            m = (r + l) // 2
            if not isBadVersion(m):
                l = m
            else:
                r = m
        return r
