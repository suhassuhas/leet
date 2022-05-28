class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        found = [False]*(n+1)
        for num in nums:
            found[num] = True
        for i in range(n+1):
            if found[i] == False:
                return i
        return 0