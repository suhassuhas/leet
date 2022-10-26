class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1}
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i]
            rem = total %k
            if rem not in seen:
                seen[rem] = i
            else:
                if i - seen[rem] > 1:
                    return True
            #print(seen)
        return False