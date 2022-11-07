class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possibleSol = {}
        
        for i, j in enumerate(nums):
            sub = target - j
            if sub in possibleSol:
                return [possibleSol[sub], i]
            possibleSol[j] = i;
            
        return