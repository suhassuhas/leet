class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for char in s:
            if len(stk)>0 and stk[-1] == char:
                stk.pop()
                continue
            stk.append(char)
        return "".join(stk)