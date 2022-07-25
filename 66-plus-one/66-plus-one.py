from typing import List   

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        digits[length-1] = 1 + digits[length-1]
        plus_one = (digits[length-1] == 10)
        if plus_one:
            digits[length-1] = 0

        for i in range(length-2,-1,-1):
            if plus_one:
                digits[i] += 1
            plus_one = False
            if digits[i] == 10:
                digits[i] = 0
                plus_one = True

        if plus_one:
            digits.insert(0,1)

        return digits