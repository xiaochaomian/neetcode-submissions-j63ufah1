class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        max_count, count = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count) + 1
        
            

                
        