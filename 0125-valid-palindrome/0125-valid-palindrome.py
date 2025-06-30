class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True 
         
        s = s.replace(" ", "")
        s = s.lower()
        
        letters = ""
        for i in range(len(s)):
            if s[i].isalnum():
                letters += s[i]

        if letters == letters[::-1]:
            return True
        
        return False
        