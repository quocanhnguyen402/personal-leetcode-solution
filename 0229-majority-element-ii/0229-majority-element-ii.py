class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = len(nums) // 3
        trace = {}
        res = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in trace:
                if num in res:
                    continue
                trace[num] += 1
            else:
                trace[num] = 1
            if trace[num] > count:
                    res.add(num)
        return res
