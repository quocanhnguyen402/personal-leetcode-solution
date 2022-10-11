class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        _max = float("inf")
        _min = float("inf")
        for num in nums:
            if num <= _min:
                _min = num
            elif num <= _max:
                _max = num
            else:
                return True
        return False