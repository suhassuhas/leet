class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for char in s:
            if stk and (abs(ord(char)-ord(stk[-1]))) == 32:
                stk.pop()
            else:
                stk.append(char)
        return "".join(stk)