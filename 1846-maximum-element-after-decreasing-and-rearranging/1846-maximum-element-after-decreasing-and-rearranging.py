class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        res = 1
        for i in range(1,len(arr)):
            arr[i] = min(arr[i-1] + 1, arr[i])
            res = max(res, arr[i])
        return res