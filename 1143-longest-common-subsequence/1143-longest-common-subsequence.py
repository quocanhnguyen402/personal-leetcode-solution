class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        trace = [0 for i in range(len(text1)+1)]
        for i in range(len(text1)+1):
            trace[i] = [0 for j in range(len(text2)+1)]
        for i1 in range(1,len(text1)+1):
            for i2 in range(1,len(text2)+1):
                if text1[i1-1] == text2[i2-1]:
                    trace[i1][i2] = trace[i1-1][i2-1] + 1
                else:
                    trace[i1][i2] = max(trace[i1-1][i2],trace[i1][i2-1])
        return trace[len(text1)][len(text2)]

        