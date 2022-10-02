class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        trace = []
        init = [0]
        for i in range(1,target+1):
            if i <= k:
                init.append(1)
            else:
                init.append(0)
        trace.append([])
        trace.append(init)
        for trace_index in range(2,n+1):
            # No of rolls so far = trace_index 
            _init = [0]
            for current_target in range(1,target+1):
                # No of way to roll to current_target with trace_index roll
                val = 0
                for i in range(1,k+1):
                    # If the last roll to get current_target is i
                    last_val = current_target-i
                    if last_val >= 0:
                        val += trace[trace_index-1][last_val]
                _init.append( val % (10**9 + 7) )
            trace.append(_init)
        return trace[n][target]