class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0] )
        count = 0
        output = [intervals[0]]

        # print(intervals)

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start < lastEnd:
                output[-1][1] = min(lastEnd,end)
                count += 1
            else :
                output.append([start,end])

        # print(count)

        return count