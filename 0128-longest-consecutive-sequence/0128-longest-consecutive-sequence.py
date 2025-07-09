class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) < 1):
            return 0

        numSet = set(nums)

        longest = 1

        for num in numSet:

            if(num - 1) not in numSet:
                current = num
                streak = 1

                while(current + 1) in numSet:
                    current += 1
                    streak += 1

                    longest = max(longest, streak)

        return longest