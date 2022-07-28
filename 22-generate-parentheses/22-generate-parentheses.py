class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_count,close_count = n,n
        result = []
        self.generate(result,open_count,close_count,"")
        return result

    def generate(self,result:List[str],open_count,close_count,current_str):
        if open_count == 0 and close_count == 0:
            result.append(current_str)
            return
        if open_count > 0:
            self.generate(result,open_count-1,close_count,current_str + "(")
        if close_count > open_count:
            self.generate(result,open_count,close_count-1,current_str + ")")