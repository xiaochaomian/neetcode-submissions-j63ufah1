import math
class Solution:
    def climbStairs(self, n: int) -> int:
        def choose(steps: int, twos):
            return math.factorial(steps - twos)/(math.factorial(twos)*math.factorial(steps-twos-twos))
        ans = 0
        for two in range(0, n//2 + 1):
            ans += choose(n, two)
        return int(ans)
        