class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        if(strX == strX[::-1]):
            return True
        return False