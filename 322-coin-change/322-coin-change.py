class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = {0:0}
        for total in range(1,amount+1):
            result[total] = float('inf')
            for coin in coins:
                if total - coin == 0:
                    result[total] = 1
                else:
                    if total - coin in result:
                        result[total] = min(result[total],result[total-coin] + 1)
            
        if result[amount] == float('inf'):
            return -1
        else:
            return result[amount]
        