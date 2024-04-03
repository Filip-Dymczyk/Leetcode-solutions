class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:

            if n not in seen:
                seen.add(n)
            else:
                return False

            str_n = str(n)
            temp_n = 0
            i = 0
            while i < len(str_n):
                temp_n += int(str_n[i]) ** 2
                i += 1
            n = temp_n

        return True
