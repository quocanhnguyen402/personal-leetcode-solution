class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end = nums[0]
        result = max_end
        for i in range (1,len(nums)):
            max_end = max(max_end + nums[i],nums[i])
            result = max(result,max_end)
        return result