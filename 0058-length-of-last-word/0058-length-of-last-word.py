class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sRev = s[::-1]
        wordL = 0
        for i in range(len(sRev)):
            if sRev[i] != " ":
                wordL += 1
                if i + 1 != len(sRev) and sRev[i + 1] == " ":
                    break
          


        return wordL