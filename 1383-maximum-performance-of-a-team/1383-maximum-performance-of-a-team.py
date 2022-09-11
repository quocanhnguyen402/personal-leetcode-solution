class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        set = []
        for i in range(n):
            set.append([efficiency[i],speed[i]])
        set.sort(reverse=True)

        speed_store = []
        speed_sum = 0
        result = -1
        
        for i in range(len(set)):
            eff = set[i][0]
            spd = set[i][1]
            heapq.heappush(speed_store, spd)
            speed_sum += spd
            if len(speed_store) > k:
                speed_sum -= heapq.heappop(speed_store)
            result = max(result,(eff * speed_sum))
        return result % (10**9+7)