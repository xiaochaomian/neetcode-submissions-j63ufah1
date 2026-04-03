class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalprod = 1
        zerocount = 0
        def find_total(nums):
            totalprod = 1
            for i in nums:
                if i!= 0:
                    totalprod*= i
            return totalprod
        for i in nums:
            if i == 0:
                zerocount+=1
        if zerocount == 0:
            totalprod = find_total(nums)
            ans = []
            for i in nums:
                if i == 0:
                    ans.append(0)
                else:
                    ans.append(int(totalprod/i))
            return ans
        elif zerocount == 1:
            totalprod = find_total(nums)
            ans = []
            for i in nums:
                if i == 0:
                    ans.append(totalprod)
                else:
                    ans.append(0)
            return ans
        else:
            return [0]*len(nums)
        
            