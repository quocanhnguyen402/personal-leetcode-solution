class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = [float("inf"),float("inf")]
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                tmp_target = target - nums[i]
                while left < right:
                    _sum = nums[left] + nums[right]
                    _distance = abs(_sum - tmp_target)
                    if _distance < result[1]:
                        result[0] = _sum + nums[i]
                        result[1] = _distance
                    if _distance == 0:
                        return result[0]
                    if _sum > tmp_target:
                        right -= 1
                    if _sum < tmp_target:
                        left += 1
        return result[0]
