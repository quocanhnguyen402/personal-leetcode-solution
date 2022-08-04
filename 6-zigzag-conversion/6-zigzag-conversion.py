class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        distance = numRows + numRows-2
        result = [""]*numRows
        index = 0
        while index < len(s):
            result[0] += s[index]
            if index + numRows - 1 < len(s):
                result[numRows-1] += s[index+numRows-1]
            for i in range(1,numRows-1):
                if index + i < len(s):
                    result[i] += s[index+i]
                    if index + i + (distance-2*i) < len(s):
                        result[i] += s[index + i + (distance-2*i)]
            index += distance
            
        return "".join(result)
        