class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)

        idx = 0
        while idx <= len_haystack - len_needle:
            if haystack[idx:len_needle + idx] == needle:
                return idx
            idx += 1
        return -1
    