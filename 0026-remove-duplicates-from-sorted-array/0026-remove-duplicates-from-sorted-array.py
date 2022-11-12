class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newIndex = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[newIndex] = nums[i]
                newIndex +=1
        return newIndex