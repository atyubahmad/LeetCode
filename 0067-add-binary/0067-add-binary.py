class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

        maxLen = max(len(a), len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)

        for i in range(len(a) -1, -1, -1,):
            bitA = int(a[i])
            bitB = int(b[i])

            total = bitA + bitB + carry

            resultBit = total % 2
            carry = total // 2

            result = str(resultBit) + result

        if carry:
            result = '1' + result
        
        return result