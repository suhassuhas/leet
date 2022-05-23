class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def csdn(num):
            org = num
            while num>0:
                dig = num % 10
                if dig == 0 or org % dig != 0:
                    return False
                num = num // 10
            return True
        ans = []
        for number in range(left,right+1):
            if csdn(number):
                ans.append(number)
        return ans