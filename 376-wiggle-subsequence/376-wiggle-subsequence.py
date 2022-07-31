class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        plus = [1]
        minus = [1]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                plus.append(minus[i-1]+1)
                minus.append(minus[i-1])
            elif nums[i] < nums[i-1]:
                minus.append(plus[i-1]+1)
                plus.append(plus[i-1])
            else:
                minus.append(minus[i-1])
                plus.append(plus[i-1])
        
        return max(plus[-1],minus[-1])