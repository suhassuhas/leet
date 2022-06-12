class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hset = set()
        i = 0
        currsum = 0
        result = 0
        for j in range(len(nums)):
            # handle when duplicates exist
            while nums[j] in hset:
                hset.remove(nums[i])
                currsum -= nums[i]
                i+=1
            hset.add(nums[j])
            currsum += nums[j]
            result = max(currsum,result)
        return result