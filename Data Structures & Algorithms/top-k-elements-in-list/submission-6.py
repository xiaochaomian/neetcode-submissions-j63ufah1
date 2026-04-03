class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans, final = {}, []
        for i in nums:
            if i in ans:
                ans[i]+=1
            else:
                ans[i] = 1 
        #{1:1, 2:2, 3:3}
        keys, values = ans.keys(), ans.values()
        for i, j in zip(keys, values):
            final.append([i, j])
        final.sort(key = lambda lst: lst[1], reverse=True)
        ansfinal = []
        for i in range(0, k):
            ansfinal.append(final[i][0])
        return ansfinal


        