class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end_at_i = [0]*len(nums)
        max_end_at_i[0] = nums[0]
        result = max_end_at_i[0]
        for i in range (1,len(nums)):
            max_end_at_i[i] = max(max_end_at_i[i-1] + nums[i],nums[i])
            result = max(max_end_at_i[i],result)
        return result