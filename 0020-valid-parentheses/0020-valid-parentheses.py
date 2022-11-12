class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        group = {')':'(' , '}':'{', ']':'['}
        
        for i in s:
            if i in group.values():
                stack.append(i)
            elif stack and group[i] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
                