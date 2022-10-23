class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        _set = set(nums)
        dupe_number = sum(nums) - sum(_set)
        missing_number = sum(range(1,len(nums) + 1)) - sum(_set)
        return [dupe_number, missing_number]