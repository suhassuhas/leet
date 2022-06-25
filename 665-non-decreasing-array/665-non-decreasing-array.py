class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        first = (nums[0] <= nums[1])
        
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1]:
                if first:
                    if nums[i+1] < nums[i-1]:
                        nums[i+1] = nums[i]
                    first = False
                else:
                    return False
                    
        return True