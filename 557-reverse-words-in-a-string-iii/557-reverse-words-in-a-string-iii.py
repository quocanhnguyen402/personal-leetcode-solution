class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(" ")
        result = ""
        for i in range(len(x)):
            result += self.reverse(x[i])
            if i != len(x) - 1:
                result += " "
        return result

    def reverse(self,s:str):
        pointer = len(s) - 1
        result = ""
        while pointer >= 0:
            result += s[pointer]
            pointer -= 1
        return result
        