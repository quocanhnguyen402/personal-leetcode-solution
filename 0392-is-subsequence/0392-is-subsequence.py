class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        res = 0
        for i in range(len(t)):
            if t[i] == s[res]:
                res += 1
                if res == len(s):
                    return True
        return False