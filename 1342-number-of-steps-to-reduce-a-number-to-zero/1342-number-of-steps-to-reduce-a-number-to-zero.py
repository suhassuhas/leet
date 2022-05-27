class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        a = num
        res = 0
        while a:
            res += 2 if (a&1) else 1
            a  = a >> 1
        return res - 1