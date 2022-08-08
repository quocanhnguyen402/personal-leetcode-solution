class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp_odd = [0]*(len(nums)+1)
        dp_even = [0]*(len(nums)+1)
        
        for i in range(1,len(nums)+1):
            dp_odd[i] = max(dp_even[i-1] - nums[i-1], dp_odd[i-1])
            dp_even[i] = max(dp_odd[i-1] + nums[i-1], dp_even[i-1])
        
        return max(dp_odd[-1], dp_even[-1])