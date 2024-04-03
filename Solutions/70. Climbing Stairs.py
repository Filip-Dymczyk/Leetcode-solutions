class Solution:
    def climbStairs(self, n: int) -> int:
        # Only 1's:
        res = 1

        # Number of max 2 steps at a time (e.g 6 // 2 = 3):
        num_of_2 = n // 2

        # Temporary number of 2 step climbs (starting from 1 because we already covered temp = 0 by adding 1 to result):
        temp = 1

        while temp <= num_of_2:
            # Number of 1's (e.g 6 - 2*2 = 2):
            num_of_1 = (n - temp * 2)

            # Number of possible positions for 2's (number of 1's + temporary number of 2's):
            positions = num_of_1 + temp

            # Values to be used in counting Newton's symbol:
            nominator = 1
            denominator = 1

            # Difference present in the denominator in Newton's symbol:
            diff = positions - temp

            # Boundary which will be used in counting simplified factorials:
            bound = temp + 1

            if diff > positions / 2:
                bound = diff + 1

            # Simplified factorial of nominator and denominator:
            j = 1
            for i in range(bound, positions + 1):
                nominator *= i
                denominator *= j
                j += 1

            # Value of Newton's symbol:
            res += int((nominator / denominator))
            temp += 1
        return res
