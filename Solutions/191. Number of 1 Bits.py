class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Getting logical and of last bit and 1:
            count += 1 & n

            # 1 time right shift - we lose right bit, to gain 0 on the MSB:
            n >>= 1

        return count
