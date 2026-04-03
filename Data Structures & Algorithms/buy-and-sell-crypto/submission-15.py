class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(0, len(prices)-1):
            yes = sorted(prices[i+1:], key=lambda x: x-prices[i])[-1]
            if yes-prices[i] >= ans:
                ans = yes-prices[i]
        return ans
