class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}

        for i in range(0,len(arr)):
            dp[arr[i]] = 1

        result = 0
        for i in range(0,len(arr)):
            for j in range(0,i):
                if arr[i] % arr[j] == 0:
                    k = arr[i] // arr[j]
                    if k in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[k]
            result += dp[arr[i]]
        return result % (10**9+7)