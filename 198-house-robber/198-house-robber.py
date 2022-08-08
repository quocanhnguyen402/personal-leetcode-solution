
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 0:
            return 0
            
        dp = [0,nums[0],nums[1]]
        result = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp.append(max(dp[i - 1] + nums[i],dp[i-2] + nums[i]))
            result = max(result,dp[-1])
        return result
        