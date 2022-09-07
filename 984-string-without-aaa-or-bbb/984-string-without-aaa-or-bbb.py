class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def createResult(bigger_number,bigger_letter,smaller_number,smaller_letter):
            result = []
            while bigger_number > 0:
                result.append("")
                result[-1] += bigger_letter
                bigger_number -= 1
                if bigger_number > 0:
                    result[-1] += bigger_letter
                    bigger_number -= 1
            while smaller_number > 0:
                for i in range(len(result)):
                    result[i] += smaller_letter
                    smaller_number -= 1
                    if smaller_number == 0:
                        break
            return "".join(result)
        
        if b > a:
            return createResult(b,"b",a,"a")
        else:
            return createResult(a,"a",b,"b")