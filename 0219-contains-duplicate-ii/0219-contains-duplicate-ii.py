class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        trace = {}
        for i in range(len(nums)):
            if nums[i] in trace:
                if i - trace[nums[i]] <= k:
                    return True
            trace[nums[i]] = i
        return False
            