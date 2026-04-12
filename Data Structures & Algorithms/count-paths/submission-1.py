import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rights = m-1
        left = n-1
        combos = math.factorial(m-1+n-1) / math.factorial(m-1) / math.factorial(n-1)
        return int(combos)