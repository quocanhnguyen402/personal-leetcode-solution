import math   

class Solution:
    def isHappy(self, n: int) -> bool:
        past_sum = set()
        while (sum := self.calSumSquare(n)) not in past_sum:
            if sum == 1:
                return True
            past_sum.add(sum)
            n = sum

        return False

    def calSumSquare(self,n:int):
        sumSquare = 0
        while n > 0:
            digit = n % 10
            sumSquare += pow(digit,2)
            n =  math.floor(n / 10)
        return sumSquare