class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # Pointer for unique elements
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1
                nums[i] = nums[j]  # Move it to the correct position
        
        return i + 1  # Number of unique elements

        