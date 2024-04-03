class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        nominator = 1
        denominator = 1

        for i in range(max(m - 1,  n - 1) + 1, n + m - 2 + 1):
            nominator *= i
        for i in range(2, min(m - 1, n - 1) + 1):
            denominator *= i
        return nominator // denominator
