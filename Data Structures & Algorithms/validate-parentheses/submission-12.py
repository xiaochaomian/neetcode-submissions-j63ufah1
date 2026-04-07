class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            val = s[i]
            if val == "(" or val == "[" or val == "{":
                stack.append(val)
            else:
                if stack == []:
                    return False
                elif val == ")" and stack[-1] != "(":
                    return False
                elif val == "]" and stack[-1] != "[":
                    return False
                elif val == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return (stack == [])



        