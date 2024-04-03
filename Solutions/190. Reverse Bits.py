class Solution:
    def reverseBits(self, n: int) -> int:
        bit_n = bin(n)[2:][::-1]

        i = 0
        pow_i = 31
        res = 0

        while i < len(bit_n):
            res += (int(bit_n[i]) * 2) ** pow_i
            i += 1
            pow_i -= 1
        return res
