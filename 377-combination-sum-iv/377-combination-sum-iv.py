class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memory = {0:1}
        for total in range(1, target + 1):
            memory[total] = 0
            for n in nums:
                memory[total] += memory.get(total - n,0)
        return memory[target]