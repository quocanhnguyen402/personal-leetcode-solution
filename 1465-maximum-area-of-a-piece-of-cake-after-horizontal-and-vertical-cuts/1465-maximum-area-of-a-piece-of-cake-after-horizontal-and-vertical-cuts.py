class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        MOD = 1000000007
        a =  (self.get_max_diff(horizontalCuts,h) * self.get_max_diff(verticalCuts,w)) % (MOD)
        return int(a)

    def get_max_diff(self, cuts: List, size: int):
        cuts.sort()
        cuts.append(size)
        max_diff = cuts[0]
        for i in range(0, len(cuts)-1):
            max_diff = max(max_diff, cuts[i+1]-cuts[i])
        return max_diff