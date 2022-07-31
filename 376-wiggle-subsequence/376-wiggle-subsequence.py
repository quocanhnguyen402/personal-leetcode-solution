class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        plus = 1
        minus = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                plus = minus+1
            if nums[i] < nums[i-1]:
                minus = plus+1
        
        return max(plus,minus)