class Solution(object):
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        max_len = 0
        # nums1 is row
        # nums2 is column
        trace  = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if nums1[i-1] == nums2[j-1]:
                    trace[i][j] = trace[i-1][j-1] + 1
                    max_len = max(trace[i][j],max_len)
                else:
                    trace[i][j] = 0
        return max(max(row) for row in trace)