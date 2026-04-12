class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-2] + val(i), dp[i-1])
        # dp[0] = val(0), dp[1] = max(val(0), val(1))
        length = len(nums) - 1
        if length+1 == 1:
            return nums[0]
        stored_dp = [-1]*(length+1)
        stored_dp[0] = nums[0]
        stored_dp[1] = max(nums[0], nums[1])


        def dp(x):
            if stored_dp[x] == -1:
                stored_dp[x] = max(dp(x-2) + nums[x], dp(x-1))
            return stored_dp[x]
        
        
        return dp(length)
