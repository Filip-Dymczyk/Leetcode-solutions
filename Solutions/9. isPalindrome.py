class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)

        left_ptr = 0
        right_ptr = len(str_x) - 1

        while left_ptr < right_ptr:
            if str_x[left_ptr] != str_x[right_ptr]:
                return False
            left_ptr += 1
            right_ptr -= 1
        return True

