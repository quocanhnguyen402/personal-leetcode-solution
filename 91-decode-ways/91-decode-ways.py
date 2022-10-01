class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        else:
            trace = [0 for x in range(len(s) + 1)] 
            trace[0] = 1
            trace[1] = 0 if s[0] == "0" else 1
            for i in range(2,len(s)+1):
                # One step jump
                if 1 <= int(s[i-1]) <= 9:
                    trace[i] += trace[i-1]
                # Two step jump
                if 10 <= int(s[i-2]) * 10 + int(s[i-1]) <= 26:
                    trace[i] += trace[i-2]
            return trace[-1]