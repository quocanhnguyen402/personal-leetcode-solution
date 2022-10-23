class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = set()
        res = [-1,-1]
        _sum = 0
        _intened_sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            visited.add(nums[i])
            _intened_sum += i + 1
        res[0] = _sum - sum(visited)
        res[1] = _intened_sum - sum(visited)
        return res