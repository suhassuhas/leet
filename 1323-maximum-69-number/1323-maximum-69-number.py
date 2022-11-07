class Solution:
    def maximum69Number (self, num: int) -> int:
        numstr = str(num)
        for i in range(len(numstr)):
            if numstr[i] == '6':
                numstr = numstr[:i]+'9'+numstr[i+1:]
                break
        return int(numstr)