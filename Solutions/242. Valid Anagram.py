from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs = Counter(s)
        ts = Counter(t)
        return cs == ts
