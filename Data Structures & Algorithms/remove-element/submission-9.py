class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length, i = len(nums), 0
        while i < length and length > 0:
            if nums[i] == val:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return len(nums)