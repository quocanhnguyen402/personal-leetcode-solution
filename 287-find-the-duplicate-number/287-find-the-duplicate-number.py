class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        trace = {}
        for i in range(0,len(nums)):
            if nums[i] not in trace:
                trace[nums[i]] = ""
            else:
                return nums[i]