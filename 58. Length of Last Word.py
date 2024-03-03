class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            s_tab = s.split()
            return len(s_tab[-1])
    