class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in range(len(accounts)): 
            if sum(accounts[i]) > max:
                max = sum(accounts[i])
                
        return max