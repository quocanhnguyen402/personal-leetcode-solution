class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        # Number of Operations
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for multi_i in range(m - 1, -1, -1):
            for left_i in range(multi_i, -1, -1):
                left = multipliers[multi_i] * nums[left_i] + dp[multi_i + 1][left_i + 1]
                right = multipliers[multi_i] * nums[n - 1 - (multi_i - left_i)] + dp[multi_i + 1][left_i]
                dp[multi_i][left_i] = max(left,right )

        return dp[0][0]