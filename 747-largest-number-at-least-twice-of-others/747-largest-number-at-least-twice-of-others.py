class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 0 if nums[0]>nums[1] else 1
        if (nums[0]>nums[1]): 
            fl,sl = 0,1
        else:
            fl,sl = 1,0
        for i in range(2,n):
            if nums[i] > nums[fl]:
                sl = fl
                fl = i
            elif nums[i] > nums[sl]:
                sl = i
        return fl if nums[fl] >= 2 * nums[sl] else -1
        
        
            