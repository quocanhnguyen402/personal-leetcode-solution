class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        res = float("inf")

        left = 0
        cur_sum = 0
        n = len(nums)

        target = sum(nums) - x

        for right in range(0, n):
            cur_sum += nums[right]

            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1

            if cur_sum == target:
                res = min(res, n - (right - left + 1))

        return -1 if res == float("inf") else res