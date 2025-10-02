class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = [w for w in s.split(" ") if w.strip()]
        return(len(string[-1]))
        