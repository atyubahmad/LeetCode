class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[0]:
                return 0
            elif target > nums[i - 1] and target < nums[i]:
                return i 
             

        return len(nums) 
        
