from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""

        strs.sort()

        for idx in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][idx] == strs[-1][idx]:
                lcp += strs[0][idx]
            else:
                break
        return lcp
    