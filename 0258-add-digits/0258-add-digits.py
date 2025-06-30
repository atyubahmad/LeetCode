class Solution:
    def addDigits(self, num: int) -> int:
        arr = []
      
        for i in str(num):
            arr.append(i)
        
        sum = 0
        flag = True
        
        while flag:
            for i in arr:
                sum += int(i)
            
            arr.clear()
            for i in str(sum):
                arr.append(i)
        
            if sum < 10:
                flag = False
                return sum
            sum = 0
    
        