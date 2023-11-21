class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(a: int):
            b = 0
            count = 0
            while a > 0:
                b = b * 10 + a % 10
                a //= 10
                count += 1
            return b

        res = 0

        revArr = collections.Counter()

        for i in range(len(nums)):
            rev_i = rev(nums[i])
            res += revArr[nums[i] - rev_i]
            revArr[nums[i] - rev_i] += 1

        return res % (pow(10,9) + 7)