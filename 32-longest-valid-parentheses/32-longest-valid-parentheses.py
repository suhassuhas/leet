class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack)>0 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        maxLen = 0
        endTerminal = n
        print(stack)
        while len(stack) != 0:
            startTerminal = stack.pop()
            maxLen = max(maxLen,endTerminal-startTerminal-1)
            endTerminal =startTerminal
        return max(maxLen,endTerminal)