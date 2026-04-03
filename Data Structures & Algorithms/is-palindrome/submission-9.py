class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for i in s:
            if i.isalnum():
                lower = i.lower()
                newstr += lower
        if newstr == newstr[::-1]:
            return True
        return False