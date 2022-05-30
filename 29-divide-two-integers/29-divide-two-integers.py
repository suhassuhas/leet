class Solution:
    '''
    100
    3
    sum =  3 6 12 24 48 96
    quot = 1 2 4  8  16 32

    recursive_func

    4
    3
    sum = 3
    quot = 1

    32 + 1 = 33

    167
    9

    sum =  9 18 36 72 144
    quot = 1 2  4  8  16

    167-144 = 22

    sum =  9 18
    quot = 1 2

    22 + 2 =24
    T(N) = O(log dividend)
    '''
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
    
        