class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in zip(*strs):
            if len(set(i)) == 1: 
                prefix += i[0]
            else: 
                return prefix
                
        return prefix
                        
            