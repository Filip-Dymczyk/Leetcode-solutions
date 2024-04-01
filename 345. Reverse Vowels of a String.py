class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l_s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in vovels:
                while s[j] not in vovels:
                    j -= 1
                l_s[i], l_s[j] = l_s[j], l_s[i]
                j -= 1
            i += 1
        return ''.join(l_s)
