class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        comp = max(arr[-1], 0)
        for i in range(len(arr)):
            index = len(arr) - i - 2 # from the back
            og = arr[index]
            arr[index] = comp
            comp = max(og, comp)

        arr[-1] = -1
        return arr
