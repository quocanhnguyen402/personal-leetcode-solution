class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        temp = 1
        cur_len = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cur_len += 1
                temp += cur_len
            else:
                cur_len = 1
                res += temp
                temp = 1
        
        return (res + temp) % 1000000007