class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            string = ""
            for i in digits:
                string += str(i)
            digits.clear()
            sum = int(string) + 1
            for i in str(sum):
                digits.append(int(i))
        return digits