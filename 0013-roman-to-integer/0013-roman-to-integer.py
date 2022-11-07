class Solution:
    def romanToInt(self, s: str) -> int:
        romToInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        totalSum = 0

        for i in range(len(s)):
            if i + 1 < len(s) and romToInt[s[i]] < romToInt[s[i + 1]]:
                totalSum -= romToInt[s[i]]
            else:
                totalSum += romToInt[s[i]]
            
        return totalSum