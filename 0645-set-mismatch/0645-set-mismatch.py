class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums = sorted(nums)
        missing,duplicate=1,-1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                duplicate=nums[i]
            elif nums[i] > nums[i-1]+1:
                missing=nums[i-1]+1
        missing = n if nums[n-1]!=n else missing
        return [duplicate,missing]