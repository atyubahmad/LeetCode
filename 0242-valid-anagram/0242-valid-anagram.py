class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        tList = []
        
        sList.extend(s)
        tList.extend(t)
        
        sList.sort()
        tList.sort()
        
        print(sList)
        print(tList)
        
        if sList == tList:
            return True
        return False