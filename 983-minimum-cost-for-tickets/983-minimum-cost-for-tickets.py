class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        trace = [0]*(days[-1] + 1)
        for day in range(1,len(trace)):
            if day > days[-1]:
                break
            if day not in days:
                trace[day] = trace[day- 1]
            else:
                # buy 1 day
                one_day = trace[day - 1] + costs[0]
                # buy 7 days
                seven_day = trace[max(day - 7,0)] + costs[1]
                # buy 30 days
                thirty_day = trace[max(day - 30,0)] + costs[2]
                trace[day] = min(one_day,seven_day,thirty_day)
        return trace[-1]