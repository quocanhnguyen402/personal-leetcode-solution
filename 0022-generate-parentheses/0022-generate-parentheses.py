class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string,open_count, close_count):
            if len(string) == 2 * n and close_count == open_count:
                res.append(string)
            else:
                if open_count < n:
                    dfs(string + "(",open_count + 1,close_count)
                if close_count < open_count:
                    dfs(string + ")",open_count,close_count + 1)

        dfs("",0,0)
        return res