class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if sorted(list(set(nums))) != nums:
            return True
        return False