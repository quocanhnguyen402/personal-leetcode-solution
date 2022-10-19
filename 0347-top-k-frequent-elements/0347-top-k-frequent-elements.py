class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _hash = {}
        for i in range(len(nums)):
            if nums[i] in _hash:
                _hash[nums[i]] += 1
            else:
                _hash[nums[i]] = 1
        result = sorted(_hash, key = lambda element : _hash[element], reverse = True)
        return result[:k]