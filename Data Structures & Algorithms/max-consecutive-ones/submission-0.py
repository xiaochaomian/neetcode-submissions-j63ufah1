class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        count, max_count = 0, 0
        for i in range(length):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                max_count = max(max_count, count)
                count = 0
        max_count = max(max_count, count)
        return max_count