class Solution:
    def reverse(self, x: int) -> int:
        ans = 0

        if x > 0:
            strInt = str(x)
            rev = strInt[::-1]
            ans = int(rev)
        
        else:
            val = abs(x) 
            strInt = str(val)
            rev = strInt[::-1]
            ans = int(rev) - int(rev) - int(rev)

        if ans < -2**31 or ans > (2**31) - 1:
            return 0

        return ans