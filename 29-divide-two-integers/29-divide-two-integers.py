class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def longDivision(a,b):
            if a<b:
                return 0
            sumI = b
            count = 1
            while(2*sumI<a):
                sumI = sumI + sumI
                count = count + count
            return count + longDivision(a-sumI,b)
        
        sign = -1 if ((dividend * -1) > 0) ^ ((divisor  * -1) > 0) else 1
        a,b = abs(dividend),abs(divisor)
        cnt = longDivision(a,b)
        
        if cnt >= 2 ** 31:
            return 2147483647 if sign > 0 else -2147483648
        return cnt if sign > 0 else -cnt
    
        