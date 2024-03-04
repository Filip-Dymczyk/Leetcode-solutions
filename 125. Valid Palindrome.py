class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:
            l_char = s[i]
            r_char = s[j]

            if l_char.isalnum() and r_char.isalnum():
                if l_char.isalpha():
                    l_char = l_char.lower()
                if r_char.isalpha():
                    r_char = r_char.lower()

                if l_char != r_char:
                    return False

                i += 1
                j -= 1

            if not l_char.isalnum():
                i += 1

            if not r_char.isalnum():
                j -= 1

        return True
