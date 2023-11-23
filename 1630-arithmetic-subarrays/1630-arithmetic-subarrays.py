class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        def checkArithmetic(l, r):
            sub = nums[l:r+1]
            if len(sub) < 2:
                return False
            sub.sort()
            diff = sub[1] - sub[0]
            for i in range(2, len(sub)):
                if sub[i] - sub[i - 1] != diff:
                    return False
            return True

        res = []
        for i in range(len(l)):
            res.append(checkArithmetic(l[i], r[i]))
        return res