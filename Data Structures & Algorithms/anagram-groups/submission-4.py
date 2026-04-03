class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            original = string
            string = list(string)
            string.sort()
            new = ''.join(string)
            if new in hashmap.keys():
                hashmap[new].append(original)
            else:
                hashmap[new] = [original]
        ans = []
        for key in hashmap:
            ans.append(hashmap[key])
        return ans