class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        left = [1] * length
        right = [1] * length
        
        left[0] = nums[0]
        right[-1] = nums[-1]
        
        for i in range(1,length):
            left[i] = left[i-1] * nums[i]
            
        for i in range(length-2,-1,-1):
            right[i] = right[i+1] * nums[i]
            
        for i in range(1,length-1):
            nums[i] = left[i-1] * right[i+1]
        nums[0] = right[1]
        nums[-1] = left[-2]
        print(left)
        print(right)
        return nums