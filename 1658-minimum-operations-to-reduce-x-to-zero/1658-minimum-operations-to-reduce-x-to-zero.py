class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, 0 
        n =len(nums)
        rollsum = sum(nums) - x
        if rollsum == 0:
            return n 
        currsum = 0
        maxlen = 0
        for r in range(n):
            currsum += nums[r]
            
            while l<n and currsum > rollsum:
                currsum -= nums[l]
                l+=1
            if currsum == rollsum:
                maxlen = max(maxlen,r-l+1)
        
        if maxlen == 0:
            return -1
        
        return n - maxlen